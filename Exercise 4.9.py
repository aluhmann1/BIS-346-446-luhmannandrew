#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 4.9

Created on Fri Jan  6 07:44:33 2023

@author: andrewluhmann3
"""
def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print('Celcius', '\t','Fahrenheit')

for celsius in range(101):
    print(f'{celsius:7}{fahrenheit(celsius):12.1f}')
