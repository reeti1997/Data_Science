# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:42:31 2018

@author: reeti
"""

import re

list1 = []
while True:
    
    str1 = raw_input()
    if not str1:
        break
    list1.append(str1)
    
    
for item in list1:
    regex = re.compile(r'^[+-]?[0-9]*\.[0-9]+$')
        
    response = regex.search(item)
    # "response" allocates a memory location to our element.
    if response:
        # print response.group()
        # this is used to show our element which is present at that given location.
        print "True"
    else:
        print "False"