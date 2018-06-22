# -*- coding: utf-8 -*-
"""
Created on Wed May 16 13:53:22 2018

@author: reeti
"""

numbers = raw_input()
arr = numbers.split(",")
list1 = []
count = 0

for item in arr:
    x = int(item)
    list1.append(x)
    count = count+1
print count
list1.sort()

#since now the list is sorted, remove the min and max element
list1.remove(min(list1))
list1.remove(max(list1))
print list1

total = 0

for item in list1:
    total = total+item
    
result = total/(count-2)
#since 2 elements are removed from the list, i.e., min and max
print result
    