# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 12:45:56 2018

@author: reeti
"""

import matplotlib.pyplot as plt
import pandas as pd

# Impoorting the dataset
dataset = pd.read_csv('Income_Data.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

# Splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Fitting Simple Linear Regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = regressor.predict(features_test)

# Model Score
Score = regressor.score(features_test, labels_test)


# Visualising the Training set results
plt.scatter(features_train, labels_train, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Income vs ML-Experience (Training set)')
plt.xlabel('ML-Experience')
plt.ylabel('Income')
plt.show()

# Visualising the Test set results
plt.scatter(features_test, labels_test, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Income vs ML-Experience (Test set)')
plt.xlabel('ML-Experience')
plt.ylabel('Income')
plt.show()