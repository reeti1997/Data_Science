# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:08:37 2018

@author: reeti
"""

import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Cars.csv')
X = dataset.iloc[:,1:].values
y = dataset.iloc[:,0].values



# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)

# Saving into different .csv files

