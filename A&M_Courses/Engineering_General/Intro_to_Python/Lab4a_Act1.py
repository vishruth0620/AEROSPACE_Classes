#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 08:32:07 2020

@author: vishruth
"""
# Teammate Names: Hunter Spier, Liliano Salgado, Michael Camacho, Vishruth Balaji
# Assignment Lab 4a Activity 1
# Section: ENGR 102-451
# Date: September 7, 2020

########## Part A ##########

a = 1 / 7
print(a)
b = a * 7
print(b)
# Yes, because multiplying the value of a by 7 would equal 1.

c = 2 * a
d = 5 * a
e = c + d
print(e)
# No, because when ythe answer .9999 is repeating.

from math import *
x = sqrt(1 / 3)
print(x)
y = x * x * 3
print(y)
z = x * 3 * x
print(z)
# The value for y has no round-off error and equals 1, but the value of z has a round off error of .99 repeating.

########## Part B ##########

TOL = 1e-10
# Check if b and e are equal within specified tolerance
if abs(b-e) < TOL:
    print('b and e are equal within tolerance of', TOL)
else:
    print('b and e are NOT equal within tolerance of', TOL)

if abs(y-z) < TOL:
    print('y and z are equal within tolerance of', TOL)
else:
    print('y and z are NOT equal within tolerance of', TOL)