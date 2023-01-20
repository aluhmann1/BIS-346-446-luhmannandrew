#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 00:36:08 2023

@author: andrewluhmann3

import numpy as np

data = [1, 10, 100, 1000, 10_000, 100_000, 10_000_000]

for i in range(len(data)):
    print('For' , data[i], 'repetitions'', the list method takes:')
    %timeit sum([x for x in range(i)])
    print('For' , data[i], 'repetitions'', the array method takes:')
    %timeit np.arange(i).sum()

"""

import numpy as np

data = [1, 10, 100, 1000, 10_000, 100_000, 10_000_000]

for i in range(len(data)):
    print('To sum x for x in a range of', data[i] ,'using the list method takes:')
    %timeit sum([x for x in range(i)])
    print('To np.arange for a range of', data[i] ,'using the array method takes:')
    %timeit np.arange(i).sum()