# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 11:22:40 2018

@author: reeti
"""

# Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing dataset
dataset = pd.read_csv('Position_Salaries.csv')
features = dataset.iloc[:, 1:2].values
labels = dataset.iloc[:, 2].values


# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features, labels)

print "Predicting result with Linear Regression",lin_reg.predict(6.5)[0]


# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg.predict(features), color = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# Fitting Polynomial Reegression to the dataset
from sklearn.preprocessing import PolynomialFeatures
# Create the polynomial features using above class
poln_object = PolynomialFeatures(degree = 4)
features_poln = poln_object.fit_transform(features)


# Once you have the poln_matrix read, imput it to linear regressor
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poln, labels)

print ("Predicting reult with Polynomial Regression",)
# Need to convert 6.5 into polynomial features
print (lin_reg_2.predict(poln_object.fit_transform(6.5)))


# Visualising the Polynomial Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poln_object.fit_transform(features)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
features_grid = np.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape((-1,1))
plt.scatter(features, labels, color = 'red')
plt.plot(features_grid, lin_reg_2.predict(poln_object.fit_transform(features_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

