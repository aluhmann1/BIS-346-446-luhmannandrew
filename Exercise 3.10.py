#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 3.10

Created on Fri Jan  6 07:34:06 2023

@author: andrewluhmann3
"""
principal = 1000.0
rate = 0.07

for year in range(1, 31):
    print(f'Amount after {year} year(s): {principal * (1 + rate) ** year:.2f}')