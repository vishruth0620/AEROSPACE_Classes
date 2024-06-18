#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:09:08 2020

@author: vishruth
"""
# Teammate Names: Hunter Spier, Liliano Salgado, Michael Camacho, Vishruth Balaji
# Name: Vishruth Balaji
# Assignment Lab 3a Activity 1f
# Section: ENGR 102-451
# Date: August 31, 2020

#Inputs the value of Fahrenheit and converts it to Celcius
user_Fahrenheit = float(input('Please enter the number of Fahrneheit to be converted to Celcius: ')) #Fahrenheit
user_Celcius = ((user_Fahrenheit - 32) * (5/9)) #Celcius
user_Celcius = '%.2f' % (user_Celcius)
print()
print(user_Fahrenheit, 'Fahrenheit is equivalent to',user_Celcius, 'Celcius.')
