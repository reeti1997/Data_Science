# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 12:51:17 2018

@author: reeti
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('input.txt', delim_whitespace = True, header=None)
data.columns = ["MPG", "Cylinders", "Displacement", "HorsePower", "Weight", "Aceeleration",
                "ModelYear", "Origin", "Car Name"]

maxi = max(data["MPG"])
print data["Car Name"] [data["MPG"] == maxi]

df = data.drop("Car Name", axis = 1)

df["HorsePower"] = df["HorsePower"].replace("?", df["HorsePower"].mode()[0])

features = df.iloc[:,1:].values
labels = df.iloc[:,0].values


from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
features = sc.fit_transform(features)
features = sc.transform(features)

# Decision Tree----------
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(features, labels)

label_pred = regressor.predict(features)

# Random Forest----------
from sklearn.ensemble import RandomForestRegressor
ran_reg = RandomForestRegressor(n_estimators = 10, random_state = 0)
ran_reg.fit(features, labels)

label_preds = ran_reg.predict(features)

# Prediction---------
f = (np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1))
labels_pred1 = regressor.predict(f)
labels_pred2 = ran_reg.predict(f)