#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 01:55:58 2019

@author: raghav
"""


import pandas as pd 
import matplotlib.pyplot as plt


data = pd.read_csv("4.csv") 

product_list = ["SYNTHETIC FIBRES / YARN", "POLYMERS", 
                "SYNTHETIC RUBBER", "PERFORMANCE PLASTICS", 
                "FIBRE INTERMEDIATES","BUILDING BLOCKS- OLEFINS"]
    
    
fig = plt.figure(figsize=(16,10))
data1 = (data.iloc[0:9,3:]).values
data2 = (data.iloc[10:17,3:]).values
data3 = (data.iloc[17:21,3:]).values
data4 = (data.iloc[23:29,3:]).values
data5 = (data.iloc[30:34,3:]).values
data6 = (data.iloc[36:42,3:]).values


plt.boxplot([data1, data2, data3,data4,data5,data6], labels = product_list,patch_artist=True,vert=True)
plt.xticks(rotation=20)

plt.title('Box Plot for comparing production of Petrochemical Products')

plt.ylabel('Production in numbers')
plt.grid()
plt.savefig("box_plot.png")
plt.show()

