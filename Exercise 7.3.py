#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 01:58:08 2023

@author: andrewluhmann3
"""

import numpy as np

numbers1 = np.arange(2, 19, 2).reshape(3, 3)

print(numbers1)

numbers2 = np.arange(9, 0, -1).reshape(3, 3)

print(numbers2)

array = numbers1 * numbers2

print(array)