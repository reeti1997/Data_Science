# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:37:29 2018

@author: reeti
"""

str1 = raw_input()
vowel = ['A','a','E','e','I','i','O','o','U','u',' ']

def translate():
    x = []
    for item in str1:
        if item in vowel:
            x.append(item)
        else:
            x.append(item+"o"+item)
            
    return "".join(x)

translate()


#ALTERNATIVE
str1 = raw_input()
vowel = "AaEeIiOoUu "

def translate(): 
    str2 = ""
    for item in str1:   
        if item in vowel:
            str2 = str2+item
        else:
            str2 = str2+item+"o"+item
            
    return str2
    
translate()