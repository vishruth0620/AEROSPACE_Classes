#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:38:06 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Michael Camacho, Liliana Salgado
# Course Header: Eng 102-451
# Assignment: Lab 7a Activity 1
# Date: 9/28/2020


#### Part A ####
#Input stock prices in one line
stock_prices = input('Enter stock prices: ').split()
new_list_Floats = []

#Changing the string inputs into a list with float numbers
for item in stock_prices:
    new_list_Floats.append(float(item))

#Iterating the numbers through the for loop to print them out 
for i in range(len(new_list_Floats)):
    print('$%7.2f' % (new_list_Floats[i]))

#### Part B ####

#Reusing the list variable new_list_Floats 
two_character_Separator = input('Enter a two-character separator: ')

#Iterating the numbers through the for loop to print them out with a two character separator
for i in range(len(new_list_Floats)):
    
    if(i == 0):
        print('%.2f ' % (new_list_Floats[i]), end = two_character_Separator)
        
    elif(i < len(new_list_Floats) - 1):
        print(' %.2f ' % (new_list_Floats[i]), end = two_character_Separator)
    
    else:
        print(' %.2f' % (new_list_Floats[i]))