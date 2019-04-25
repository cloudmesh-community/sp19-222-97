from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import csv
import graphviz
import io
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO
from __init__ import code_dir

url = 'https://drive.google.com/uc?export=download&id=1flTTzCX8aZOOX11CidgUvZcc_VrQTAi5'

# Source: https://github.com/cloudmesh/cloudmesh-nn/blob/master/cloudmesh/nn/service/data.py
def download_data(url, filename):
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    return

def download(output):
    data_dir = code_dir + '/data'
    out_file = data_dir + output
    download_data(url_ex_2, out_file)
    return str(output) + " downloaded to " + str(code_dir)

# Source: https://realpython.com/python-csv/
# Save as .txt
def read_csv():
    with open('./data/TETRIS_DOWNLOAD.csv') as csv_file:
        # entries = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        print(headers)
        featureList = []
        labelList = []
        # line_count = 0
        for row in csv_reader:
            labelList.append(row[len(row) - 1])
            rowDict = {}
            for i in range(1, len(row) - 1):
                rowDict[headers[i]] = row[i]
        featureList.append(rowDict)

        #print(featureList)
    return featureList, labelList

# Save as image
def data_tree():
    featureList = []
    labelList = []

    featureList, labelList = read_csv()

    # Vectorize features and print out features names
    vec = DictVectorizer()
    X = vec.fit_transform(featureList).toarray()
    print("X: ", X)
    print(vec.get_feature_names())

    # Vectorize class labels and print out label names
    print("labelList: " + str(labelList))
    lb = preprocessing.LabelBinarizer()
    Y = lb.fit_transform(labelList)
    print("Y: " + str(Y))

    # Use the decision tree for classification
    clf = tree.DecisionTreeClassifier(criterion='gini')
    clf.fit(X, Y)
    print("clf: " + str(clf))

    dot_data = tree.export_graphviz(clf, out_file = './output/DT_GRAPH.png', feature_names=vec.get_feature_names())
    graph = graphviz.Source(dot_data)
    # graph.render(filename='./output/DT_GRAPH.png')
