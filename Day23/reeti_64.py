# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:23:17 2018

@author: reeti
"""

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris = load_iris()
iris = iris.data

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
iris = pca.fit_transform(iris)

explained_variance = pca.explained_variance_ratio_

# Clustering
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0) 
y_kmeans = kmeans.fit_predict(iris)

plt.scatter(iris[y_kmeans == 0, 0], iris[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Iris Setosa')
plt.scatter(iris[y_kmeans == 1, 0], iris[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Iris Versicolor')
plt.scatter(iris[y_kmeans == 2, 0], iris[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Iris Virginica')
'''Versicolor n Virginica are showing almost same attributes,
    We cnt differentiate them on the basis of data we have.
    So we can just pressume.'''

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of species')
plt.xlabel('Features')
plt.ylabel('Species')
plt.legend()
plt.show()