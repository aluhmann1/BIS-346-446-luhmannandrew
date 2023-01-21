#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 09:09:58 2023

@author: andrewluhmann3
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

bananas = pd.read_csv("Bananas.csv")
print(bananas)

bananas['DATE'] = pd.to_datetime(bananas['DATE'],
                              infer_datetime_format=True)

plt.scatter(bananas['DATE'],bananas['Bananas price per lb'],color='red',
            marker='^')
plt.rc('xtick', labelsize=8)
plt.ylabel('Bananas price per lb')
plt.xlabel('Date')
plt.title('Banana Prices in US')

plt.show()
