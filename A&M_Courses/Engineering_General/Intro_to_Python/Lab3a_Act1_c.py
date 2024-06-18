#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 10:17:56 2020

@author: vishruth
"""
# Teammate Names: Hunter Spier, Liliano Salgado, Michael Camacho, Vishruth Balaji
# Name: Vishruth Balaji
# Assignment Lab 3a Activity 1c
# Section: ENGR 102-451
# Date: August 31, 2020

#Inputs the value of pascals and converts it to millimeters of mercury
user_Pascals = float(input('Please enter the number of Pascals to be converted to millimeters of mercury: ')) #Pascals
user_mm_Mercury = (user_Pascals * 0.00750062) #millimeters of mercury
user_mm_Mercury = '%.2f' % (user_mm_Mercury)
print()
print(user_Pascals, 'Pascals is equivalent to', user_mm_Mercury,'millimeters of mercury.')