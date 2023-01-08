#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:25:43 2023

@author: andrewluhmann3

"""
dollars = int(input('Enter quantity of Dollars you wish to convert: '))
    
def pounds(dollars):
    return 0.84 * dollars
def euros(dollars):
    return 0.95 * dollars
def canadian(dollars):
    return 1.36 * dollars

print(f'{dollars} Dollars is equal to {pounds(dollars):.2f} British Pounds.')
print(f'{dollars} Dollars is equal to {euros(dollars):.2f} Euros.')
print(f'{dollars} Dollars is equal to {canadian(dollars):.2f} Canadian Dollars.')

