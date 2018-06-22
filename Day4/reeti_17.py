# -*- coding: utf-8 -*-
"""
Created on Wed May 16 12:40:24 2018

@author: reeti
"""

from PIL import Image
img = Image.open("sample1.jpg")
img = img.convert('LA').show()

grayscale = grayscale.rotate(270).show()

from PIL import ImageFilter
