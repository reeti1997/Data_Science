# -*- coding: utf-8 -*-
"""
Created on Wed May 30 10:29:34 2018

@author: reeti
"""

import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv',
     header=None,
     usecols=[0,1,2]
    )

df.columns = ['Class Label','Alcohol','Malic Acid']

features = df.iloc[:,1:].values
labels = df.iloc[:,0].values

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels, test_size = 0.2, random_state = 0)

# You can use only one scaling algo at a time.
# STANDARD SCALER------------
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#features_train = sc.fit_transform(features_train)
#features_test = sc.transform(features_test)


# MINMAX SCALER--------------
from sklearn.preprocessing import MinMaxScaler
mmx = MinMaxScaler()
features_train = mmx.fit_transform(features_train)
features_test = mmx.transform(features_test)
