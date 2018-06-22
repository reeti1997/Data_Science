# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:03:19 2018

@author: reeti
"""

value = input("Enter no. of small and big bricks and target: ")
data = list(value)
small = 1
big = 5
def bricks() : 
    if(data[0]*small + data[1]*big) >= data[2]:
        return True
    else:
        return False
    
bricks()
