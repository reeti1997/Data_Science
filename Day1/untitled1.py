# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:25:02 2018

@author: reeti
"""

str1 = """triple quotes strings are also called doc strings in python"""
#can be multilined
#used for documentation

str2 = """Forsk Jaipur"""
str2[0] = 'f'
#Error : 'str' object doesnt support item assignment
#this is because strings in python are immutable, i.e., they cannot be chnaged

print str2.upper()
#this changes str2 in all uppercase letters
#this contradiscts the fact
#no. because the real string is still the same. only the o/p has changed

print str2[-2]
#prints value from last

print str2[::-1]
#reversing the string

print str2[::-3]
#print in reverse but after 3 hops

str1 = """madam"""
print str1.find('a')

str1.replace('a', 'A')
#this replaces a with A but original string remains unchanged

str3 = "Welcom to summer bootcamp 2018"
str3.split()
#output : ['Welcom', 'to', 'summer'.......]
#this is an array. but in python we call it a "LIST".
#split() doesnt hv any parameter passed so it splits according to space
str3.split('m')
#output : ['Welco', 'to su', '', 'er bootca', 'p 2018']

type(str3.split())
#o/p : list

'boot' in str3
#"in" checks the presence of any substring in given string n is case sensitive.

" ".join(['hello','world'])
#o/p : 'hello world'
"-".join(['hello','world'])
#o/p : 'hello-world'
#any symbol can be used in ""

a = 'hello'
b = 'python'
print "%s %s" % (a,b)
#o/p : hello python
print 'Chapter %d: %s' % (2,'Machine Learning')
#o/p : Chapter 2: Machine Learning

