#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise  3.01

Created on Fri Jan  6 07:25:07 2023

@author: andrewluhmann3
"""
passes = 0

for student in range(10):
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    while result != 1 and result != 2:  
        print('Incorrect result entered.')
        result = int(input('Enter result (1=pass, 2=fail): '))
        
    if result == 1:
        passes = passes + 1

print('Passed:', passes)
print('Failed:', 10 - passes)

if passes > 8:
    print('Bonus to instructor')
