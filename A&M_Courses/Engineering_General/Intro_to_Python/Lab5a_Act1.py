#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:41:20 2020

@author: vishruth
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 5a Activity 1
# Date: 9/14/2020

# Five Test Cases

# 1. x^3 - x^2 + x - 1 , [-1,4]
# 2. -4x^3 + 3x^2 + 25x + 6 , [-3,4]
# 3. x^3 - 6x^2 - 2x + 12 , [11,14]
# 4. 8x^3 - 2x^2 - 5x - 7 , [-1,2]
# 5. 2x^3 + 3x^2 - 2x - 3 , [0,4]

import matplotlib.pyplot as plt
import numpy as np

#Inputting coefficients for the cubic polynomial and its intervals
coefficient_A = int(input('Please enter the coefficient A: ')) #Inputting the first coefficient
coefficient_B = int(input('Please enter the coefficient B: ')) #Inputting the second coefficient
coefficient_C = int(input('Please enter the coefficient C: ')) #Inputting the third coefficient
coefficient_D = int(input('Please enter the coefficient D: ')) #Inputting the fourth coefficient
lower_bound_Interval = int(input('Please enter the lower bound of the interval: ')) #Inputting the lower bound interval
upper_bound_Interval = int(input('Please enter the upper bound of the interval: ')) #Inputting the upper bound interval

# Coefficients for cubic polynomial
A = coefficient_A
B = coefficient_B
C = coefficient_C
D = coefficient_D

# x axis bounds to plot
x1 = lower_bound_Interval
x2 = upper_bound_Interval

# Generate data for plotting
xvals = np.arange(x1, x2, 0.1)
yvals = A * xvals ** 3 + B * xvals ** 2 + C * xvals + D

# plot the results  
plt.plot(xvals, yvals,'b')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Plot of Cubic Polynomial')
plt.axvline(x=0, c='k')
plt.axhline(y=0, c='k')
plt.grid(True)
plt.show()

f_x1 = A * x1 ** 3 + B * x1 ** 2 + C * x1 + D
f_x2 = A * x2 ** 3 + B * x2 ** 2 + C * x2 + D

#Checking if there isn't a root between the intervals
if ((f_x1 < 0 and f_x2 < 0) or ((f_x1 > 0 and f_x2 > 0))):
    print('\nThere is no root between the intervals.')

#Calculating the root
else:
    x = x1
    change_LB = x1
    change_RB = x2
    tolerance = 10**-6
    iteration_Counter = 0
    while (x <= x2):
        iteration_Counter += 1
        y = A * x ** 3 + B * x ** 2 + C * x + D
        if(-1 < y < 1): #Negative Slope Test Case
            if (y < tolerance):
                if (change_LB < x):
                    change_LB = x
            if (y > -(tolerance)): #Positive Slope Test Case
                if (change_RB > x):
                    change_RB = x
            x += (10**-6)
        x += .1
    if(change_LB == x1):
        change_LB = change_RB
    
    elif(change_RB == x2):
        change_RB = change_LB
            
    x_midPoint = (change_LB + change_RB) / 2
    #Printing the root and number of iterations to calculate the root
    print('\nThe root is %1.3f.' % (x_midPoint))
    print('It took',iteration_Counter,'iterations to find the root.')
            
            
            
            
            
        
    
    
    
