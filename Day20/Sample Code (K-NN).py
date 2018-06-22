# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 10:22:27 2018

@author: reeti
"""

# K-Nearest Neighbors (K-NN) 
# Importing the libraries 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# Importing the dataset 
data = pd.read_csv("Social_Network_Ads.csv") 
features = data.iloc[:, 2:-1].values 
labels = data.iloc[:, -1].values 

# Splitting the dataset into the Training set and Test set 
from sklearn.model_selection import train_test_split 
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.25,random_state=0) 

# Feature Scaling 
from sklearn.preprocessing import StandardScaler 
sc = StandardScaler() 
features_train = sc.fit_transform(features_train) 
features_test = sc.transform(features_test) 

# Fitting K-NN to the Training set 
from sklearn.neighbors import KNeighborsClassifier 
classifier = KNeighborsClassifier(n_neighbors=5, p=2) 
classifier.fit(features_train, labels_train)
 
# Predicting the Test set results 
pred = classifier.predict(features_test) 

# Making the Confusion Matrix 
from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(labels_test, pred) 

# Getting Model Score 
Score = classifier.score(features_test, labels_test)
 
# Visualising the Training set results 
from matplotlib.colors import ListedColormap 
features_set, labels_set = features_train, labels_train
features1, features2 = np.meshgrid(np.arange(start = features_set[:, 0].min()- 1,
                                             stop = features_set[:, 0].max()+ 1, step = 0.01), np.arange(start = features_set[:, 1].min()- 1,
                                             stop = features_set[:, 1].max()+ 1, step = 0.01))
plt.contourf(features1, features2, classifier.predict(np.array([features1.ravel(), features2.ravel()]).T).reshape(features1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(features1.min(), features1.max())
plt.ylim(features2.min(), features2.max())
for i, j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set == j, 0], features_set[labels_set == j, 1],
c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('K-NN (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show() 


# Visualising the Test set results 
from matplotlib.colors import ListedColormap 
features_set, labels_set = features_test, labels_test
features1, features2 = np.meshgrid(np.arange(start=features_set[:,0].min()-1,
                                             stop=features_set[:,0].max()+1, step=0.01), np.arange(start = features_set[:,1].min()-1,
                                             stop=features_set[:,1].max()+1, step=0.01)) 
plt.contourf(features1,features2, classifier.predict(np.array([features1.ravel(),features2.ravel()]).T).reshape(features1.shape),
             alpha=0.75,cmap = ListedColormap(('red', 'green'))) 
plt.xlim(features1.min(), features1.max())
plt.ylim(features2.min(), features2.max()) 
for i,j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set==j,-0], features_set[labels_set==j,1],
c=ListedColormap(('red','green'))(i),label=j) 
plt.title("K-NN (Test set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show() 