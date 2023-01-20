#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 02:03:32 2023

@author: andrewluhmann3
"""

import numpy as np

numbers = np.arange(1, 16).reshape(3, 5)

print('Original table for reference:\n', numbers[:])
print('a.\n', numbers[2])

print('b.\n', numbers[:, 4])

print('c.\n', numbers[:, 0:2])

print('d.\n',  numbers[:, 2:5])

print('e.\n', numbers[1, 4])

print('f.\n', numbers[1:3, [0, 2, 4]])
