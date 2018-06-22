# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:45:42 2018

@author: reeti
"""


import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 20.0, 10000)
print incomes

plt.hist(incomes, 50)
plt.show()

print np.mean(incomes)
print np.median(incomes)


incomes = np.append(incomes, [1000000000])

print np.median(incomes)
print np.mean(incomes)

