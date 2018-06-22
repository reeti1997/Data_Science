# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:29:39 2018

@author: reeti
"""

value = input()

for i in range(0,value):
    for j in range(0,i+1):
        print "*",
    print ""
    
for i in range(0,value):
    for y in range(value-1,i,-1):
        print "*",
    print ""
        