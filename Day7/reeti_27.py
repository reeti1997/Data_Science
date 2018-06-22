# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:13:56 2018

    


@author: reeti
"""

val = raw_input()

val1 = val.split(" ")

if all(int(num)>0 for num in val1):
    if any(num==num[::-1] for num in val1):
        print True
    else:
        print False
else:
    print False


