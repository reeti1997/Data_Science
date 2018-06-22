# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:32:08 2018

@author: reeti
"""

always remember that the working diretory should be same.
#OPENING a file
#SYNTAX : open(filename, mode)
#by default, we have read mode. so its OK not to mention read
#we hv to specify an object that can be used in our code
fp = open("test.txt")

type(fp)
#o/p : file

fp.read()
#reads the content of the file
#o/p : 

print fp.read()
#this wont print anything because while reading the file previously, the cursor reached on the last position.
#so there is nothing to print

fp.close()
#closes the connection.
#no more funtion can be applied. we have to reopen the file.

fp.readline()
#reads the content of the file line by line from the current cursor position.
#o/p : 'Machine learning\n'
#it is a string

#WE USE "SEEK" TO SET THE CURSOR POSITION DYNAMICALLY.
#SYNTAX : obj.see(offset, from_what)
#"from_what" can have the values : 0,1,2
#0 = Beginning of the file
#1 = Current
#2 = End of the file

fp.seek(0,0)
#cursor at the beginning of top left corner.
fp.readline()
#read from the beginning

fp.readlines()
#output is in the form of a list.

#we can also read the lines in file using for loop
for line in fp:
    print line
    
#WRITE MODE
fp = open("test.txt", 'w')
#two things happen
#1: If the file is already created, all the content will be lost.
#2: Creates a new file with the mentioned name if it is currently not present.
#If we want our old data, we use "APPEND" instead of write.

fp.write("Machine Learning class")
#this wont write anything in our file.
#all the statements are stored in the buffer until close() is called.
fp.close()
#now the contents will be written in file.



























