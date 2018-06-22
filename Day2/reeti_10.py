# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:43:17 2018

@author: reeti
"""

str1 = raw_input()
length = len(str1)
if length == 0:
    print "0"

str2 = str1.split(",")
print str2

a = 0

for a in range(0,7):
    #item1 = int(item)
    #print item1
    #print item
    if str2[a] == 13:
        str2.remove(str2[a])
        print str2
        a = a+1
        
    else:
        print "xyz"
        
        
    
    
for item in range(0,length):
    print str1[item]
    if x[item]==13:
        x.remove(item)
        x.remove()
        x.remove(x[item-1])
        
    else:
        sum = sum+x[item]
        
print sum