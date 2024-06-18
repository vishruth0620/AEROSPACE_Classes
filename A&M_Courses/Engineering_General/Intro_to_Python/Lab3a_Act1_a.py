#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 09:20:26 2020

@author: vishruth
"""
# Teammate Names: Hunter Spier, Liliano Salgado, Michael Camacho, Vishruth Balaji
# Name: Vishruth Balaji
# Assignment Lab 3a Activity 1a
# Section: ENGR 102-451
# Date: August 31, 2020

#Inputs the value of Newtons and converts it to Pounds
user_Newtons = float(input('Please enter the number of Newtons to be converted to pounds (force): ')) #Newtons
user_Pounds = (user_Newtons * 0.224809) #Pounds
user_Pounds = '%.2f' % (user_Pounds)
print()
print(user_Newtons, 'Newtons is equivalent to', user_Pounds,'pounds of force.')
