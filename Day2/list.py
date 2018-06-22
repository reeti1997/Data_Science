#DAY_3

x=[1,2,3]
print type(x)
#this is a list
#indexing is also present in list
print x[0]
#o\p : 1

print x[0:2]
#o/p : [1,2]
#Slicing is possible in list

x[0]=10
#this is possible. list is mutable.
#Therefore, many operations can be performed on list.
#the current item is replaced.

x.append(12)
print x
#o/p : [1,2,3,12]
#item is added in the last position using append

x.remove(2)
print x
#the value of item is written n not its index
#o/p : [1,3,12]
x.remove(20)
print x
#this is a ValueError
#o/p : list.remove(x): x not in list

x.insert(2,15)
print x
[1,3,15,12]

3 in x
#o/p : True
3 not in x
#o/p : False

x.pop()
#pops the last value in list
#if list is empty, then IndexError is generated
#o/p : pop from empty list

y = [1,2,3, 'SKIT', 'POORNIMA', 'JECRC', 'BMIT', 'AIC']
y.sort()
print y
#the original list is sorted.
#unlike in string where only the output was changed and the original string was immutable.
#o/p : [1,2,3,'AIC', 'BMIT', 'JECRC', 'POORNIMA'', 'SKIT']

y.reverse()
print y
#sort in reverse order
#o/p : ['SKIT', 'POORNIMA', 'JECRC', 'BMIT', 'AIC', 3, 2, 1]

a=[1,2,3]
b=[4,5,6]
a.append(b)
print a
#o/p : [1, 2, 3, [4, 5, 6]]
#Entire list is appended as a single item.

a[3]
#o/p : [4,5,6]
a[3][1]
#o/p : 5

a.extend(b)
#this appends elements of b in a one by one


#LIST COMPREHENSION
a = [1,2,3]
[x**2 for x in a]
#o/p : [1, 4, 9]
[x+1 for x in [x**2 for x in a]]
#o/p : [2, 5, 10]
#this is NESTED LIST COMPREHENSION




















