#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 10:10:32 2020

@author: vishruth
"""
# Teammate Names: Hunter Spier, Liliano Salgado, Michael Camacho, Vishruth Balaji
# Name: Vishruth Balaji
# Assignment Lab 3a Activity 1b
# Section: ENGR 102-451
# Date: August 31, 2020

#Inputs the value of BTUs and converts it to joules
user_BTUs = float(input('Please enter the number of BTUs to be converted to joules: ')) #BTUs
user_Joules = (user_BTUs * 1055.06) #Joules
user_Joules = '%.2f' % (user_Joules)
print()
print(user_BTUs, 'BTUs is equivalent to', user_Joules,'joules.')
