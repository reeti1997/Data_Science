# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 10:23:02 2018

@author: reeti
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

dataset = pd.read_csv('PastHires.csv')
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
for i in [1,3,4,5]:
    features[:,i] = labelencoder.fit_transform(features[:,i])

labels = labelencoder.fit_transform(labels)


from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(features, labels)

label_pred = regressor.predict(features)

from sklearn.ensemble import RandomForestRegressor
ran_reg = RandomForestRegressor(n_estimators = 10, random_state = 0)
ran_reg.fit(features, labels)

# f = (np.array([10,1,4,0,1,0]).reshape(1,-1))
f = (np.array([10,0,4,1,0,1]).reshape(1,-1))
labels_pred = ran_reg.predict(f)

