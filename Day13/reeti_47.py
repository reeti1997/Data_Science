# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:32:56 2018

@author: reeti
"""

import pandas as pd
data = pd.read_csv("Loan.csv")
data = data.drop("Loan_ID", axis = 1)

features = data.iloc[:,:-1].values
labels = data.iloc[:,-1].values

for i in ["Gender","Married","Dependents","Education","Self_Employed","Property_Area","Target"]:
    data[i] = data[i].astype('category')
    data[i] = data[i].cat.codes

#data["Gender"] = data["Gender"].astype('category')
#data["Gender"] = data["Gender"].cat.codes
#
#data["Married"] = data["Married"].astype('category')
#data["Married"] = data["Married"].cat.codes
#
#data["Dependents"] = data["Dependents"].astype('category')
#data["Dependents"] = data["Dependents"].cat.codes
#
#data["Education"] = data["Education"].astype('category')
#data["Education"] = data["Education"].cat.codes
#
#data["Self_Employed"] = data["Self_Employed"].astype('category')
#data["Self_Employed"] = data["Self_Employed"].cat.codes
#
#data["Property_Area"] = data["Property_Area"].astype('category')
#data["Property_Area"] = data["Property_Area"].cat.codes
#
#data["Target"] = data["Target"].astype('category')
#data["Target"] = data["Target"].cat.codes

one_hot = pd.get_dummies(data["Property_Area"])
data = data.drop("Property_Area", axis = 1)
data = data.join(one_hot)


from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


