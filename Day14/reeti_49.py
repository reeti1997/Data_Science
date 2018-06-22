# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:56:42 2018

@author: reeti
"""

import pandas as pd
data = pd.read_csv("Red_Wine.csv")


for i in data:
    data[i] = data[i].fillna(data[i].mode()[0])
    
features = data.iloc[:,:-1].values
labels = data.iloc[:,-1].values
    
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,0] = labelencoder.fit_transform(features[:,0])

from sklearn.preprocessing import OneHotEncoder
one_hot = OneHotEncoder(categorical_features = [0])
features = one_hot.fit_transform(features).toarray()

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)
