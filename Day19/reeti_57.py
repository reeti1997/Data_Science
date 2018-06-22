# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 10:22:57 2018

@author: reeti
"""


import pandas as pd
import numpy as np

data = pd.read_csv("affairs.csv")
features = data.iloc[:,:-1].values
labels = data.iloc[:,-1].values

from sklearn.preprocessing import OneHotEncoder
for i in [-2,-1]:
    one_hot = OneHotEncoder(categorical_features = [i])
    features = one_hot.fit_transform(features).toarray()
    features = features[:,1:]


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)
Score = classifier.score(features_test, labels_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

data["affair"].value_counts(normalize = 1)

# predict the probability
label_ran = classifier.predict_proba(np.array([1,0,0,0,0,0,0,1,0,0,3,25,3,1,4,9]).reshape(1,-1))

# Predict the best model
import statsmodels.formula.api as sm
features = np.append(arr = np.ones((6366,1)).astype(int), values = features, axis = 1)
features_opt = features[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
classifier_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
classifier_OLS.summary()

features_opt = features[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15]]
classifier_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
classifier_OLS.summary()

features_opt = features[:,[0,1,2,3,4,5,7,8,9,10,11,12,13,15]]
classifier_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
classifier_OLS.summary()

features_opt = features[:,[0,1,2,4,5,7,8,9,10,11,12,13,15]]
classifier_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
classifier_OLS.summary()

features_opt = features[:,[0,1,2,4,7,8,9,10,11,12,13,15]]
classifier_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
classifier_OLS.summary()

features_opt = features[:,[0,1,2,7,8,9,10,11,12,13,15]]
classifier_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
classifier_OLS.summary()

features_opt = features[:,[0,2,7,8,9,10,11,12,13,15]]
classifier_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
classifier_OLS.summary()

features_opt = features[:,[0,2,7,9,10,11,12,13,15]]
classifier_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
classifier_OLS.summary()

features_opt = features[:,[0,7,9,10,11,12,13,15]]
classifier_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
classifier_OLS.summary()


