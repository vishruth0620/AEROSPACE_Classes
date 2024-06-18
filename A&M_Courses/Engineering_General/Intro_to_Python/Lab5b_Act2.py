#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 00:00:42 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 5b Activity 2
# Date: 9/14/2020

num = int(input('Please enter an integer: ')) #Input an integer from the user

first_Number = 0 #Setting first number to 0
second_Number = 1 #Setting second number to 1
print('The first %d estimates of the Golden ratio are:' % (num)) #Printting number of esimates from num as beginning statement
for i in range(1, num + 1): #Using for loop from 1 to the number plus 1
        next_Number = first_Number + second_Number #Setting next number to add first number and second number
        golden_Ratio = next_Number / second_Number #Setting Golden Ratio to divide next number to second number
        if (i < num) :
            print('%3.3f' % (golden_Ratio), end = ', ')#Printing out the Golden Ratio
        else :
            print('%3.3f' % (golden_Ratio), end = '')#Printing out the Golden Ratio
            
        first_Number = second_Number #Setting first number to second number
        second_Number = next_Number #Setting second number to next number
    
    