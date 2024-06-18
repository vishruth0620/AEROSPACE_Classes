#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:48:19 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 4b Activity 4
# Date: 9/11/2020

import math 

value_A = ''
value_B = ''
value_C = ''
equation_A = ''
equation_B = ''

coefficient_A = int(input('Please enter the coefficient A: ')) #Inputting the first coefficient
coefficient_B = int(input('Please enter the coefficient B: ')) #Inputting the second coefficient
coefficient_C = int(input('Please enter the coefficient C: ')) #Inputting the third coefficient
  
if (coefficient_A != 0) : #Creating the first term (x^2)
  
    if (coefficient_A == -1):
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

if (coefficient_A == 0 and coefficient_B == 0) : #Check whether coefficient a and b are 0 to prove that there is an invalid combination leading to no roots
     print('You entered an invalid combination of coefficients!')

else :

    get_Discriminant  = (coefficient_B ** 2) - (4 * coefficient_A * coefficient_C) #Finding the discriminant of quadratic equation
    
    #Check if the discrminant has an imaginary number and print the root in the form of a + bi
    if (get_Discriminant < 0) :
        part_1 = (-coefficient_B / (2 * coefficient_A))
        part_2 = math.sqrt(abs(get_Discriminant)) / (2 * coefficient_A)
        print('\nThe roots of the equation {}{}{}{}{} = 0 is x = {} + {:.1f}i.'.format(value_A,equation_A,value_B,equation_B,value_C,part_1,part_2))
    
    else :
        if (coefficient_A != 0) : #If all coefficent doesn't contain zero, then its a trinomial equation and prints out two roots
             root_1 = ((-coefficient_B) - math.sqrt(get_Discriminant))//(2*(coefficient_A))
             root_2 = ((-coefficient_B) + math.sqrt(get_Discriminant))//(2*(coefficient_A))
             if (root_1 == root_2): #If two roots are the same in the trinomial equation, then it combines into one root and prints it out
                 root_Same = root_1
                 print('\nThe roots of the equation {}{}{}{}{} = 0 is x = {}.'.format(value_A,equation_A,value_B,equation_B,value_C,root_Same))
             
             else :
                 print('\nThe roots of the equation {}{}{}{}{} = 0 are x = {} and x = {}.'.format(value_A,equation_A,value_B,equation_B,value_C,root_1,root_2))
        
        elif (coefficient_A == 0) : #If the first coefficient for the first term is zero, then it's a linear equation and prints out only one root
             root_3 = (-coefficient_C) / (coefficient_B)
             print('\nThe roots of the equation {}{}{}{}{} = 0 is x = {}.'.format(value_A,equation_A,value_B,equation_B,value_C,root_3))
    
    
    
    

