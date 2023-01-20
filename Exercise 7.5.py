#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 02:01:26 2023

@author: andrewluhmann3
"""

import numpy as np

powers = np.array([2 ** i for i in range(6)]).reshape(2, 3)

print(powers)

print(powers.flatten())

print(powers.ravel())

print(powers)