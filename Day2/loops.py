# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:05:36 2018

@author: reeti
"""

a = 10

if a < 13:
    print "Hi"
    print a
else:
    print 'Bye'
    

x = [1,2,4,5,6,7]

for item in x:
    print item
#for each item in x, print item.
#item is not an index. any variable can be used in place of item.
#this prints each item in x.
    
a = 10
while a<20:
    print a
    a = a+1
    