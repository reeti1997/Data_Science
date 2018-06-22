# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:23:15 2018

@author: reeti
"""

import pandas as pd
data = pd.read_csv("Automobile.csv")

# 01-------------
print data.dtypes

# 02-------------
df1 = data.select_dtypes(include = ['object'])

# 03-------------
for i in data:
    data[i] = data[i].fillna(data[i].mode()[0])
    
# 04-------------
val = 0
for i in ["convertible","hardtop","hatchback","sedan","wagon"]:
    data["body_style"][data["body_style"]==i] = val
    val += 1
    
features = data.iloc[:,:-1].values
labels = data.iloc[:,-1].values
    
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

i=0
while i<25:
    features[:,i] = labelencoder.fit_transform(features[:,i])
    i+=1
    
from sklearn.preprocessing import OneHotEncoder
one_hot = OneHotEncoder(categorical_features = [6])
features = one_hot.fit_transform(features).toarray()

one_hot = OneHotEncoder(categorical_features = [7])
features = one_hot.fit_transform(features).toarray()

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

    
