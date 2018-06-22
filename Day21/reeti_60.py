# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:19:52 2018

@author: reeti
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("deliveryfleet.csv")
features = data.iloc[:,1:3].values

# 01-------------
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0) 
y_kmeans = kmeans.fit_predict(features)

plt.scatter(features[y_kmeans == 0, 0], features[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[y_kmeans == 1, 0], features[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of drivers')
plt.xlabel('Speeding_Feature')
plt.ylabel('Distance_Feature')
plt.legend()
plt.show()

# 02-------------
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0) 
y_kmeans = kmeans.fit_predict(features)

plt.scatter(features[y_kmeans == 0, 0], features[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Rural Non-Distant')
plt.scatter(features[y_kmeans == 1, 0], features[y_kmeans == 1, 1], s = 100, c = 'cyan', label = 'Rural Distant')
plt.scatter(features[y_kmeans == 2, 0], features[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Urban Distant')
plt.scatter(features[y_kmeans == 3, 0], features[y_kmeans == 3, 1], s = 100, c = 'blue', label = 'Urban Non-Distant')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of drivers')
plt.xlabel('Speeding_Feature')
plt.ylabel('Distance_Feature')
plt.legend()
plt.show()