# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 11:26:50 2018

@author: reeti
"""

import pandas as pd
import numpy as np

data = pd.read_csv("mushrooms.csv")
features = data[["odor", "population", "habitat"]].values
labels = data.iloc[:,0].values.reshape(-1,1)

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
for i in [0,1,2]:
    features[:,i] = labelencoder.fit_transform(features[:,i])

from sklearn.preprocessing import OneHotEncoder
for i in [0,-2,-1]:
    one_hot = OneHotEncoder(categorical_features = [i])
    features = one_hot.fit_transform(features).toarray()
    features = features[:,1:]
    
from sklearn.model_selection import train_test_split 
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0) 

from sklearn.neighbors import KNeighborsClassifier 
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) 
classifier.fit(features_train, labels_train)
 
# Predicting the Test set results 
pred = classifier.predict(features_test) 

# Making the Confusion Matrix 
from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(labels_test, pred) 

# Getting Model Score 
Score = classifier.score(features_test, labels_test)


#-----------------------
features = data.iloc[:,1:].values
labels = data.iloc[:,0].values


from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
for i in range(len(features[0])):
    features[:,i] = labelencoder.fit_transform(features[:,i])

labels = labelencoder.fit_transform(labels)

import statsmodels.formula.api as sm
features = np.append(arr = np.ones((8124,1)).astype(int), values = features, axis = 1)
features_opt = features[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]]

df = pd.DataFrame(features_opt,dtype="float64")
features_opt = df.iloc[:,:].values

classifier_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
classifier_OLS.summary()

#to be continued--------------



