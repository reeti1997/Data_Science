# -*- coding: utf-8 -*-
"""
Created on Mon May 28 10:24:59 2018

@author: reeti
"""

import urllib2
url1 = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"

page = urllib2.urlopen(url1)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page)

all_tables = soup.find_all('table')
right_table = soup.find('table', class_= 'wikitable')
# spaces are present in the class name.
# this means multiple classes are present.
# so we take the first name.

A = []
B = []
C = []

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    #data = row.findAll('td')
    if len(cells) == 7:
    # 3 shows that 3 td are prsent.
        A.append(cells[0].find(text=True))
        B.append(cells[1].text.strip())
        C.append(cells[4].text.strip())
        
import pandas as pd

df = pd.DataFrame(A,columns=['Rank'])
# this is the formt of the dataFrame that we have defined.
df['State/Territory'] = B
df['National Share(%)'] = C

df1 = df.iloc[0:6]
print df1


import matplotlib.pyplot as plt

values = df1['National Share(%)']
labels = df1['State/Territory']
explode = [0.1,0,0,0,0,0]
plt.pie(values, labels=labels, explode=explode, autopct='%1.2f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
