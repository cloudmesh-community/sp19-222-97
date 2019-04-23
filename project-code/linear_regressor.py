from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import csv
import io
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st

url_ex_0 = 'https://drive.google.com/uc?export=download&id=1flTTzCX8aZOOX11CidgUvZcc_VrQTAi5'
url_ex_1 = 'https://drive.google.com/uc?export=download&id=1FEvUuHcvDk54hsJ4gu69K4wkJQn14m-8'
url_ex_2 = 'https://drive.google.com/uc?export=download&id=1U6Hdsm4_bWFkZCEidAl1V49GqTpC7ENF'

# Source: https://github.com/cloudmesh/cloudmesh-nn/blob/master/cloudmesh/nn/service/data.py
def download_data(url, filename):
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    return

# download_data(url_ex_2, './data/TETRIS_DOWNLOAD.csv')

# Source: https://realpython.com/python-csv/
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

    print(f'Processed {line_count} lines.')
    return entries

def linear_regression():
    entries = read_csv
    scores = []
    rounds = []
    for e in entries:
        scores.append(e[3])
        rounds.append(e[4])

        #plt.plot(rounds, scores, '.')
        #plt.yscale('linear')
        #plt.xscale('linear')
        #plt.show()

        N = len(entries)
        n = len(entries[0])

        data = np.zeros((N,n-1))
        Features = np.zeros((N,n-2))
        Labels = np.zeros((N,))

        for k in range(N):
            for i in range(n-1):
                data[k,i] = float(entries[k][i])

        np.random.shuffle(entries)

        for k in range(1,4):
            plt.plot(data[:,k], data[:,0], 'b.')
            lin_regress_stats = stats.linregress(data[:,k], data[:,0])
            print(lin_regress_stats)
            plt.title(str(k));
            # plt.savefig("feature" + str(k) + ".png" , dpi=300)
            plt.show()
