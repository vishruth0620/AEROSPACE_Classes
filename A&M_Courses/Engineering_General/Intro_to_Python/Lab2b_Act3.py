#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:20:36 2020

@author: vishruth
"""
# Name: Vishruth Balaji
# Assignment Lab 2b Activity 3
# Section: ENGR 102-451


#Starting off by finding the output of 1
x = 1
z = 0
z += x
print(z, '\n')

#Calculating and printing the output of 24
y = 10
x += 1
y *= x
z += y
x += 1
z += x
print(z, '\n')

#Calculating and printing the output of 321
z = 0
y = 10
x = y
y *= x
x = 1
x += 1
x += 1
y *= x
z += y
y = 10
x = y
y += x
z += y
x = 1
z += x
print(z, '\n')

#Calculating and printing the output of 10^16
z = 0
y = 10
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
z += y
print(z, '\n')

#Calculating and printing the output of 1234
z = 0
y = 10
x = y
y *= x
y *= x 
z += y
y = 10
y += x
y *= x
z += y
y = 10
y += x
y += x
z += y
x = 1
x += 1
x += 1
x += 1
z += x
print(z)
