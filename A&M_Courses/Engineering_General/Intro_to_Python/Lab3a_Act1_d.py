#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 10:37:43 2020

@author: vishruth
"""
# Teammate Names: Hunter Spier, Liliano Salgado, Michael Camacho, Vishruth Balaji
# Name: Vishruth Balaji
# Assignment Lab 3a Activity 1d
# Section: ENGR 102-451
# Date: August 31, 2020

#Inputs the value of Revolutions per second and converts it to hertz
user_revolutions_Second = float(input('Please enter the number of Revolutions per second to be converted to hertz: ')) #Revolutions per second
user_Hertz = (user_revolutions_Second * 1.0) #hertz
user_Hertz = '%.2f' % (user_Hertz)
print()
print(user_revolutions_Second, 'Revolutions per second is equivalent to', user_Hertz,'hertz.')
