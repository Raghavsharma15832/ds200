#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 01:26:07 2019

@author: raghav
"""

import pandas as pd 
import matplotlib.pyplot as plt


data = pd.read_csv("1.csv") 

mydata = data.iloc[108:123,2:7]

m, n = mydata.shape
Em_D = []
Dm_D= []

Em_O = []
Dm_O= []

for i in range(m):
    Em_D.append(mydata.iloc[i,0])
    Dm_D.append(mydata.iloc[i,1])
    Em_O.append(mydata.iloc[i,3])
    Dm_O.append(mydata.iloc[i,4])
    
    
fig = plt.figure(figsize=(10,10))
plt.scatter(Em_D, Dm_D, s=6, c='green', alpha=0.5, label = " Domestic")
plt.scatter(Em_O, Dm_O, s=6, c='red', alpha=0.5, label = "Overseas")
plt.title('Scatter plot for Pessenger embarked and disembarked on Major Ports .com')
plt.xlabel('Pessenger embarked')
plt.ylabel('Pessenger disembarked')
plt.grid()
plt.legend(loc='upper left', borderaxespad=0.)
plt.savefig("Scatter_plot.png")
plt.show()

