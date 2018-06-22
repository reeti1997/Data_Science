# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:00:36 2018

@author: reeti
"""


#FOR COMPRESSION AND DECOMPRESSION
import zlib

s = "Python is used to extensively in industry"
len(s)

t = zlib.compress(s)
#output is gibberish, i.e., in hex file format.
#length is compressed
#it can be tranferred to another system.
#then we decompress it.

zlib.decompress(t)
#we get our string.



#FOR IMPORTING SOMETHING FROM ANY WEBSITE
import urllib2

urllib2("http://www.forsk.in")

f = urllib2.urlopen("http://www.forsk.in")

f.read(1000)
#shows that we have to read the first 1000 bytes from the webpage.



#USED FOR BASIC FUNCTIONS
import os
os.getcwd()
#this gets the current working directory



#IMAGE PROCESSING
from PIL import Image

# Saving the file in different format
img_filename = Image.open("sample1.jpg")
img_filename.show()


from PIL import ImageFilter
img_filename.filter (ImageFilter.BLUR).show()
#apply various filters.

img_filename.size

img_filename.format

img_filename.mode

































