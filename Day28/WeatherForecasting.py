# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:22:25 2018

@author: reeti
"""

import urllib2
wiki="https://www.wunderground.com/history/airport/VIDD/2018/6/1/DailyHistory.html?req_city=Delhi&req_state=&req_statename=India&reqdb.zip=&reqdb.magic=&reqdb.wmo="
page= urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="obs-table")
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
for row in right_table[0].findAll('tr'):
    cells=row.findAll('td')
    if cells != []:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
import pandas as pd
df=pd.DataFrame(A,columns=['Time'])
df['Delhi']=B
print df

import urllib2
wiki="https://www.wunderground.com/history/airport/VIDD/2018/6/1/DailyHistory.html?req_city=Meerut&req_state=UP&req_statename=India&reqdb.zip=00000&reqdb.magic=29&reqdb.wmo=42139"
page= urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="obs-table")

for row in right_table[0].findAll('tr'):
    cells=row.findAll('td')
    if cells != []:
        
        C.append(cells[1].text.strip())

import pandas as pd
df['Meerut'] = C    


import urllib2
wiki="https://www.wunderground.com/history/airport/VIDD/2018/6/1/DailyHistory.html?req_city=Noida&req_state=UP&req_statename=India&reqdb.zip=00000&reqdb.magic=62&reqdb.wmo=42182"
page= urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="obs-table")

for row in right_table[0].findAll('tr'):
    cells=row.findAll('td')
    if cells != []:
        
        D.append(cells[1].text.strip())
import pandas as pd

df['Noida']=D



import urllib2
wiki="https://www.wunderground.com/history/airport/VIDD/2018/6/1/DailyHistory.html?req_city=Ghaziabad&req_state=UP&req_statename=India&reqdb.zip=00000&reqdb.magic=58&reqdb.wmo=42182"
page= urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="obs-table")

for row in right_table[0].findAll('tr'):
    cells=row.findAll('td')
    if cells != []:
        
        E.append(cells[1].text.strip())

df['Ghaziabad']=E
  


