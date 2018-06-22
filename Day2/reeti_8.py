# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:46:43 2018

@author: reeti
"""

str1 = raw_input()
#Take theinput string as "Python 3.2"
#Initialise our counters
Letters = 0
Digits = 0

for item in str1:
    if item.isalpha()==True:
    #if the value is an alphabet, increase the counter by 1
        Letters = Letters+1
        
    elif item.isdigit()==True:
    #if the value is a digit, increase the counter by 1
        Digits = Digits+1

#print the values of counter which gives the number of letters and digits.        
print "Letters ",Letters
print "Digits ",Digits
        