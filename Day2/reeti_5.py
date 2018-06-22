# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:35:12 2018

@author: reeti
"""

x= raw_input()
#take input in the form of string so that it can be splitted
y = x.split(",")
print "List : ",y
#we get a list when we split a string
y = tuple(y)
print "Tuple : ",y   
#typecasting
