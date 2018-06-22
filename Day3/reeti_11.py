# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:26:55 2018

@author: reeti
"""

value = input()
#taking inputs
value1 = list(value)
print value1
#typecast tuple into list

def Add(x,y) : return x+y

def Multiply(x,y) : return x*y

def Largest(x,y) : return max(x,y)

def Smallest(x,y) : return min(x,y)

def Sorting() :
    value1.sort()
    return value1.sort() 

def Remove_Duplicates() : return set(value1)


#defining Print()       
def Print() :
    print "Sum = ",reduce(Add, value1)
    print "Multiply = ",reduce(Multiply, value1)
    print "Largest = ",reduce(Largest, value1)
    print "Smallest = ",reduce(Smallest, value1)
    print "Sorted = ",Sorting()
    print "Without Duplicates = ", Remove_Duplicates()
   
#Calling Print()
Print()   

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
