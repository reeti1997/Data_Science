# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:13:58 2018

@author: reeti
"""

# collections.Counter()
# A counter is a container that stores elements as dictionary
# and their counts are stored
# as dictionary values

# Sample code

from collections import Counter
mylist = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

print Counter(mylist)
# o/p : Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

print Counter(mylist).items()
# o/p : [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]

print Counter(mylist).keys()
# o/p : [1,2,3,4,5]

print Counter(mylist).values()
# o/p : [3,4,4,2,1]
#-----------------------------------


# dict vs defaultdict
# Since python2.5 there is new defaultdict in
# the module collections. this works similarly to
# the defaultdict method of dictionaries.

# Sample code

s = 'Some letters need to be counted'
#conventional way
d = {}
for key in s:
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
print d


#OR we can use the new defaultdict:
from collections import defaultdict
dd = defaultdict(int)
for key in s:
    dd[key] += 1
    # no else part required because it creates a new key by default if
    # its not present in it.
print dd



#--------------------------------
""" NAMEDTUPLES
Basically named tuples are easy to create,
lightweight objects types.
they turn into convinient containers for simple tasks.
with namedtuples, you dont have to use integer indices for accessing members of a tuple
"""

# code 01
from collections import namedtuple
Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
dot_product()

#-------------------------------------

#zip

#all
#any





































































