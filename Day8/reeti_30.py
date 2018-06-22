# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:54:21 2018

@author: reeti
"""

import urllib2

url1 = "https://en.wikipedia.org/wiki/ICC_Player_Rankings"

page = urllib2.urlopen(url1)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page)

all_tables = soup.find_all('table')

right_table = soup.find_all('table', class_= 'wikitable')
# find gives only the first occurance.
# so we have to use find_all


A=[]
B=[]
C=[]
D=[]

# since many tables have same class, so we have to use indexing.
# since my table is present as 4th position, so index is 3..
for row in right_table[3].findAll('tr'):
    cells = row.findAll('th')
    data = row.findAll('td')
    if len(data) == 3:
    # 3 shows that 3 td are prsent.
        A.append(cells[0].find(text=True))
        B.append(data[0].text.strip())
        C.append(data[1].text.strip())
        D.append(data[2].text.strip())
            
        
import pandas as pd

df = pd.DataFrame(A,columns=['Rank'])
# this is the formt of the dataFrame that we have defined.
df['Change'] = B
df['Name'] = C
df['Rating'] = D

print df
