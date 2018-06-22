# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:00:46 2018

@author: reeti
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("tree_addhealth.csv")

for i in data:
    data[i] = data[i].fillna(data[i].mode()[0])
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values = 'nan', strategy = 'mean', axis = 1)
#
#for i in range(len(features[0])):
#    imputer = imputer.fit(features[:,i].reshape(1,-1))
#    features = imputer.transform(features[:,i].reshape(1,-1))

# 01----------------
labels = data.iloc[:,7].values
data = data.drop("TREG1", axis = 1)
features = data.iloc[:,:15].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)
Score = classifier.score(features_test, labels_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# 02----------------
labels = data.iloc[:,-4].values
features = data.iloc[:,[0,15]].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)
Score1 = classifier.score(features_test, labels_test)

from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(labels_test, labels_pred)

# 03----------------
labels = data.iloc[:,7].values
features = data.iloc[:,1:6].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

from sklearn.ensemble import RandomForestClassifier
ran_class = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
ran_class.fit(features_train, labels_train)

labels_pred = ran_class.predict(features_test)
Score2 = ran_class.score(features_test, labels_test)

from sklearn.metrics import confusion_matrix
cm2 = confusion_matrix(labels_test, labels_pred)

