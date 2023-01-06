#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 3.16

Created on Fri Jan  6 07:35:46 2023

@author: andrewluhmann3
"""
largest = int(input('Enter number: '))
number = int(input('Enter number: '))

for i in range(2, 10):
    number = int(input('Enter number: '))

    if number > largest:
        next_largest = largest
        largest = number
    elif number > next_largest:
        next_largest = number

print(f'Largest is {largest}\nSecond largest is {next_largest}')
