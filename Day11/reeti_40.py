# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:11:04 2018

@author: reeti
"""


import numpy as np

list2 = []
list1 = raw_input().split(" ")

for item in list1:
    list2.append(int(item))
    
a = np.array(list2)
b = a.reshape(3,3) 
print b