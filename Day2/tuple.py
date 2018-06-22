a = (1,2,3,4)

a[0] = 10
#o/p : TypeError: 'tuple' object does not support item assignment
#This means that like strings, tuples are immutable.

divmod(23,5)
#o/p : (4, 3)
#it returns a tuple.
x, y = divmod(23,5)
#x will store 4
#y will store 3
#this is called UNPACKING.

x,y,z = divmod(23,5)
#not possible

x = (5)
#x is just an int
x = (5,)
#x is a tuple

a = (2, 3, 5, 6)
a.insert(2,3)
#not possible
#o/p : AttributeError: 'tuple' object has no attribute 'insert'