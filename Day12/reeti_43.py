# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:41:43 2018

@author: reeti
"""

import pandas as pd

df = pd.read_csv("Automobile.csv")
df1 = df['make'].value_counts()

import matplotlib.pyplot as plt

values = df1[:10]
labels = list(values.index)
explode = []

for item in values:
    if item == df1.max():
        explode.append(0.1)
        
    else:
        explode.append(0)

plt.pie(values, labels=labels, explode=explode)
plt.axis('equal')
plt.title('CAR MAKERS')

plt.show()
