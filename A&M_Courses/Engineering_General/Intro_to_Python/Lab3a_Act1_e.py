#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 10:57:29 2020

@author: vishruth
"""
# Teammate Names: Hunter Spier, Liliano Salgado, Michael Camacho, Vishruth Balaji
# Name: Vishruth Balaji
# Assignment Lab 3a Activity 1e
# Section: ENGR 102-451
# Date: August 31, 2020

#Inputs the value of Meters per second and converts it to miles per hour
user_meters_Second = float(input('Please enter the number of Meters per second to be converted to miles per hour: ')) #Meters per second 
user_miles_Hour = (user_meters_Second * 2.23694) #miles per hour
user_miles_Hour = '%.2f' % (user_miles_Hour)
print()
print(user_meters_Second, 'Meters per second is equivalent to', user_miles_Hour,'miles per hour.')
