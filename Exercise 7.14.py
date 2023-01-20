#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 02:11:47 2023

@author: andrewluhmann3
"""

import numpy as np

array1 = np.array([[0, 1], [2, 3]])

array2 = np.array([[4, 5], [6, 7]])

array3 = np.vstack((array1, array2))

print('a.\n', array3)

array4 = np.hstack((array1, array2))

print('b.\n', array4)

array5 = np.vstack((array4, array4))

print('c.\n',array5)

array6 = np.hstack((array3, array3))

print('d.\n',array6)