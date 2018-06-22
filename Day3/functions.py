# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:29:06 2018

@author: reeti
"""

a = [1,2]
b = [1,2]

a is b
#o/p : False
#"is" checks whether this is the same object or not. 
#it returns false because both objects are resent at different memory locations.

a == b
#o/p : True
#== used for comparison

c = a
a is c
#o/p : True
#we call it "ALIASING" in C language

# FUNCTION DEFINITION
def add_two_numbers(a, b):
    return a+b  #return statement is mandatory

# FUNCTION CALLING
add_two_numbers(2, 4)


def add(a, b):
    print a+b
add(2,3)
print add(2,3)
#o/p : 
        #5 -> from add(2,3)
        #5 -> from print a+b
        #None -> print is iyeselfa function so it also returns its type,i.e, NONE
        
def explain_python():
    """Print a message explaining about Python"""
    print('Python is not a snake')
    print('Python is a programming lang')
#o/p : 
explain_python.func_doc
#this prints the doc string
#the doc string is used only for documentation.
#o/p : 'Print a message explaining about Python'

#filter, map and reduce

range(0,10)
#gives values from 0 to 9 in form of a list.


def f(x) : return x%3 == 0 or x%5 == 0
#returns true if any one condition is satisfied
#SYNTAX : filter(function, list)
filter(f, range(2,25))
#o/p : [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]
#we get only those values where the function f(x) is true.
#in filter, the function should have a condition.


def cube(x) : return x*x*x
#returns cube of x
#SYNTAX : map(function, list)
map(cube, range(1,11))
#o/p : [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
map(f, range(1,11))
#o/p : [False, False, True, False, True, True, False, False, True, True]
#the elements in the set of inputs should be equal to elements in outputs.
#there must be an output for each input in map()


def add(x,y) : return x+y
#SYNTAX : reduce(function, list)
reduce(add, [1,2,3,4,5,6,7,8,9,10])
#first 1,2 will be parameters of add(x,y). Then 2,3 n so on.
reduce(add, range(1,11))
#o/p : 55
#reduce returns only a single value or a single object.
#map n reduce are applied together

#ANONYMOUS FUNCTION -> lambda
map(lambda x:x*x*x, range(1,11))
#o/p : [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]



words = ['it', 'is', 'raining', 'cats', 'and', 'dogs']
map(lambda x : len(x), words)
#o/p : [2, 2, 7, 4, 3, 4]




























