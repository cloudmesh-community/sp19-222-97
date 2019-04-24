from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import csv
import io
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from __init__ import code_dir

url_ex_0 = 'https://drive.google.com/uc?export=download&id=1flTTzCX8aZOOX11CidgUvZcc_VrQTAi5'
url_ex_1 = 'https://drive.google.com/uc?export=download&id=1FEvUuHcvDk54hsJ4gu69K4wkJQn14m-8'
url_ex_2 = 'https://drive.google.com/uc?export=download&id=1U6Hdsm4_bWFkZCEidAl1V49GqTpC7ENF'

# Source: https://github.com/cloudmesh/cloudmesh-nn/blob/master/cloudmesh/nn/service/data.py

def download_data(url, filename):
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    return

def download(output):
    data_dir = code_dir + '/data/'
    out_file = data_dir + output
    download_data(url_ex_1, out_file)
    return str(output) + " downloaded to " + str(code_dir)

# download_data(url_ex_2, './data/TETRIS_DOWNLOAD.csv')

# Source: https://realpython.com/python-csv/
# Save entries as a .txt
def read_csv():
    with open('./data/TETRIS_DOWNLOAD.csv') as csv_file:
        entries = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print(row)
            if line_count == 0:
                line_count += 1
            else:
                new_entry = row
                entries.append(new_entry)
                line_count += 1

    #print(f'Processed {line_count} lines.')
    f = open("./output/TETRIS_DOWNLOAD_READ.txt", "w+")
    for e in entries:
        f.write(str(e) + "\n")
    f.close()
    return entries

# Saves as .pngs
def linear_regression():
    entries = read_csv()
    # print(entries)
    scores = []
    rounds = []
    for e in entries:
        scores.append(e[3])
        rounds.append(e[4])

    N = len(entries)
    n = len(entries[0])

    data = np.zeros((N,n-1))
    Features = np.zeros((N,n-2))
    Labels = np.zeros((N,))

    for k in range(N):
        for i in range(n-1):
            data[k,i] = float(entries[k][i])

    np.random.shuffle(entries)

    fig, ax = plt.subplots(3,1)

    fig.set_figwidth(10)
    fig.set_figheight(10)

    lin_regress_stats = stats.linregress(data[:,1], data[:,0])
    ax[0].plot(data[:,1], data[:,0], 'b.')
    ax[0].set_title('Rank vs. Year')

    lin_regress_stats = stats.linregress(data[:,2], data[:,0])
    ax[1].plot(data[:,2], data[:,0], 'r.')
    ax[1].set_title('Rank vs. Score')

    lin_regress_stats = stats.linregress(data[:,3], data[:,0])
    ax[2].plot(data[:,3], data[:,0], 'g.')
    ax[2].set_title('Rank vs. Rounds Won')

    fig.savefig('./output/Linear_Regression.png')
