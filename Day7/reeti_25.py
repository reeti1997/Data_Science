# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:10:07 2018

@author: reeti
"""


list1 = []
while True:
    str1 = raw_input("Enter name, age and score :\n")
    if not str1:
        break
    tup1 = str1.split(",")
#---------------    
    tup1[1] = int(tup1[1])
    tup1[2] = int(tup1[2])
    tup2 = tuple(tup1)
    list1.append(tup2)
#---------------
    list1.apppend((tup1[0], int(tup1[1]), int(tup1[2])))  
#---------------
list1.sort()
print list1



