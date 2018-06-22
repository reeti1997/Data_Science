# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:59:12 2018

@author: reeti
"""

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(150.0, 20.0, 1000)
print incomes

plt.hist(incomes, 100)
plt.show()

print np.mean(incomes)
print np.median(incomes)

print incomes.std()
print incomes.var()