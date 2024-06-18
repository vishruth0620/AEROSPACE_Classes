#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:40:13 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 4b Activity 3
# Date: 9/9/2020


value_A = ''
value_B = ''
value_C = ''
equation_A = ''
equation_B = ''

coefficient_A = int(input('Please enter the coefficient A: ')) #Inputting the first coefficient
coefficient_B = int(input('Please enter the coefficient B: ')) #Inputting the second coefficient
coefficient_C = int(input('Please enter the coefficient C: ')) #Inputting the third coefficient

if (coefficient_A != 0) : #Creating the first term (x^2)
  
    if (coefficient_A == -1) :
        value_A = '- '
    
    elif (coefficient_A == 1):
        value_A = ''
    
    elif (coefficient_A > 1) :
        value_A = '' + str(coefficient_A)
    
    else :
        value_A = '- ' + str(abs(coefficient_A))
      
    equation_A = 'x^2'
    
        
if (coefficient_B != 0) : #Creating the second term (x)
    
    if (coefficient_B == -1) :
        value_B = ' - '
    
    elif (coefficient_B == 1 and coefficient_A != 0):
        value_B = ' + '
    
    elif (coefficient_B > 1 and coefficient_A == 0) :
        value_B = str(coefficient_B)
        
    elif (coefficient_B > 1) :
        value_B = ' + ' + str(coefficient_B)
   
    elif (coefficient_B < -1) :
        value_B = ' - ' + str(abs(coefficient_B))

    equation_B = 'x'
    
if (coefficient_C != 0) : #Creating the third term (constant number)
    
    if (coefficient_C == -1) :
        value_C = ' - ' + str(abs(coefficient_C))
    
    elif (coefficient_C >= 1 and (coefficient_A == 0  and coefficient_B == 0)) :
        value_C = str(coefficient_C)
    
    elif (coefficient_C >= 1):
        value_C = ' + ' + str(coefficient_C)
        
    else :
        value_C = ' - ' + str(abs(coefficient_C))

#Printing the quadratic equation with the combination of the three coefficients for each term
print('\nThe quadratic equation is {}{}{}{}{} = 0'.format(value_A,equation_A,value_B,equation_B, value_C))
