# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:46:44 2018

@author: reeti
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("tshirts.csv")
features = data.iloc[:,[1,2]].values

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0) 
y_kmeans = kmeans.fit_predict(features)

plt.scatter(features[y_kmeans == 0, 0], features[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Size M')
plt.scatter(features[y_kmeans == 1, 0], features[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Size L')
plt.scatter(features[y_kmeans == 2, 0], features[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Size S')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of drivers')
plt.xlabel('height (inches)')
plt.ylabel('weight (pounds)')
plt.legend()
plt.show()