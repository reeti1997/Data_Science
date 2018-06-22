# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:06:58 2018

@author: reeti
"""

import numpy as np

x = np.random.randint(low=5, high=15, size=(40,))
print x


#-----------------------------
# WITH NUMPY
count = np.bincount(x)
print np.argmax(count)


#-----------------------------
# WITHOUT NUMPY
# 01
from scipy import stats

m = stats.mode(x)
print m
#-----------------------------
# 02
#from collections import Counter
#b = Counter(x)
#y = b.most_common()

#-----------------------------
# 03
z = 0
dict1 = {}
for i in x:
    if i in dict1:
        dict1[i]+=1
        
    else:
        dict1[i]=1
        
lst = []
for i in dict1.items():
    k,v = i
    i = v,k
    lst.append(i)
lst.sort()
c,d = lst[-1]

print d