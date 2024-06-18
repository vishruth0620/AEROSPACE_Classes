#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:47:26 2020

@author: vishruth
"""
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 3b Activity 1b
# Date: 9/2/2020


#asking user for how many decimals to evaluate 2/7 to
decimals = int(input('Please enter the number of decimals to evaluate 2/7 to: '))

#calculating the answer by shiftingg the desired decimals to left of decimal point, converting to a integer to r
#remove all unwanted decimals, then moving desired decimals back into the appropriate position

calculate_Precision = int((float(2/7) * (10 ** decimals))) / (10 ** decimals)
#printing the answer
print('The value of 2/7 to', decimals, 'digits is ', calculate_Precision)