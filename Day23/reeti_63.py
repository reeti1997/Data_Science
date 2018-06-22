# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:24:46 2018

@author: reeti
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("crime_data.csv")
features = data.iloc[:,[1,2,4]].values

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)

explained_variance = pca.explained_variance_ratio_

# Clustering
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0) 
y_kmeans = kmeans.fit_predict(features)

plt.scatter(features[y_kmeans == 0, 0], features[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Murder')
plt.scatter(features[y_kmeans == 1, 0], features[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Assault')
plt.scatter(features[y_kmeans == 2, 0], features[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Rape')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters')
plt.xlabel('Features')
plt.ylabel('Cities')
plt.legend()
plt.show()