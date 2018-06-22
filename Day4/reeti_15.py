# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:26:03 2018

@author: reeti
"""

for item in range(1,51):
            
    if item%3 == 0 and item%5 == 0:
        print "FizzBuzz"
        
    elif item%3 == 0:
        print "Fizz"
        
    elif item%5 == 0:
        print "Buzz"
        
    else:
        print item
