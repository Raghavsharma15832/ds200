#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 02:55:03 2019

@author: raghav
"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("3.csv") 

states = data["State/UT"].values
visit_16 = data["2016 - Domestic"].values + data["2016 - Foreign"].values
visit_17 = data["2017 - Domestic"].values + data["2017 - Foreign"].values




Em_O = []
Dm_O= []
b=-1
s = 0
n_groups = len(states[s:b])
fig = plt.figure(figsize=(10,10))
index = np.arange(n_groups)*3
bar_width = 0.6
opacity = 0.8

rects1 = plt.bar(index, visit_16[s:b], bar_width,
alpha=opacity,
color='b',
label='2016')

rects2 = plt.bar(index + bar_width, visit_17[s:b], bar_width,
alpha=opacity,
color='g',
label='2017')

plt.title('Tourism in different states 2016 and 2017')
plt.ylabel('Number of Tourists in a year')
plt.xticks(index + bar_width,states[s:b], rotation=90)
#plt.grid()
plt.legend(loc='upper left', borderaxespad=0.)
plt.savefig("bar_graph.png")
plt.show()

