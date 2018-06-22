# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:19:40 2018

@author: reeti
"""

str1 = raw_input("Enter : ").strip()
a = str1.find(" ")
print str1[a+1:].strip(),str1[:a+1].strip()