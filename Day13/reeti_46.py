# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:12:57 2018

@author: reeti
"""

import pandas as pd
data = pd.read_csv("Loan.csv")

# LoanID is not at all useful in learning.
# so an alterative can be dropping the LoanID.
# data = data.drop("Loan_ID", axis = 0)

features = data.iloc[:,:-1].values
labels = data.iloc[:,-1].values


from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

i=0
while i<6:
    features[:,i] = labelencoder.fit_transform(features[:,i])
    i+=1


labels = labelencoder.fit_transform(labels)

features[:,-1] = labelencoder.fit_transform(features[:,-1])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[-1])
features = onehotencoder.fit_transform(features).toarray()



from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)
