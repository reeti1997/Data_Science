# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:05:30 2018

@author: reeti
"""

import numpy as np
import pandas as pd
df=pd.read_csv("Automobile.csv")
df["price"]=df["price"].fillna(df["price"].mean())

b = np.array(df["price"])
print type(b)
print df["price"].max()
print df["price"].min()
print df["price"].mean()
print df["price"].std()