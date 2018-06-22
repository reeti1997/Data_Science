# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 12:13:19 2018

@author: reeti
"""

import urllib2
wiki="https://www.timeanddate.com/weather/india/dehradun/hourly"
page= urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="zebra")
right_table_tbody = right_table[0].findAll('tbody')

A=[]
B=[]
D=[]
E=[]
F=[]
G=[]
H=[]

for row in right_table_tbody[0].findAll('tr'):
    cells=row.findAll('td')
    cells2=row.findAll('th')
    if cells != []:
        A.append(cells2[0].text.strip())
        B.append(cells[1].text.strip().split()[0])
import pandas as pd
df=pd.DataFrame(A,columns=['Time'])

df['Dehradun']=B



wiki="https://www.timeanddate.com/weather/@10552092/hourly"
page= urllib2.urlopen(wiki)

soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="zebra")

right_table_tbody = right_table[0].findAll('tbody')

for row in right_table_tbody[0].findAll('tr'):
    cells=row.findAll('td')
    if cells != []:
        E.append(cells[1].text.strip().split()[0])
        
df["Rewari"] = E

wiki="https://www.timeanddate.com/weather/india/agra/hourly"
page= urllib2.urlopen(wiki)

soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="zebra")

right_table_tbody = right_table[0].findAll('tbody')

for row in right_table_tbody[0].findAll('tr'):
    cells=row.findAll('td')
    if cells != []:
        F.append(cells[1].text.strip().split()[0])
        
df["Agra"] = F


wiki="https://www.timeanddate.com/weather/india/lucknow/hourly"
page= urllib2.urlopen(wiki)

soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="zebra")

right_table_tbody = right_table[0].findAll('tbody')

for row in right_table_tbody[0].findAll('tr'):
    cells=row.findAll('td')
    if cells != []:
        G.append(cells[1].text.strip().split()[0])
        
df["Lucknow"] = G


wiki="https://www.timeanddate.com/weather/india/new-delhi/hourly"
page= urllib2.urlopen(wiki)

soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="zebra")

right_table_tbody = right_table[0].findAll('tbody')

for row in right_table_tbody[0].findAll('tr'):
    cells=row.findAll('td')
    if cells != []:
        H.append(cells[1].text.strip().split()[0])
        
df["Delhi"] = H


features = df.iloc[:,1:-1].values
labels = df.iloc[:,-1].values

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels,
                                                                             test_size = 0.2, 
                                                                             random_state = 0)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features_train, labels_train)

labels_pred = lin_reg.predict(features_test)

Score = lin_reg.score(features_test, labels_test)

from sklearn.model_selection import cross_val_score
accuracy = cross_val_score(estimator = lin_reg, X = features_train, y = labels_train, cv = 10)
print "Mean Accuracy : ",accuracy.mean()
print accuracy.std()