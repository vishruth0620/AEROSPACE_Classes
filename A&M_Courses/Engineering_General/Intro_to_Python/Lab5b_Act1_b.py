#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:30:30 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 5b Activity 1b
# Date: 9/14/2020


sum = 0
product = 1
num = int(input('Enter an integer: ')) #Inputting an integer number from the user

for i in range(1, num + 1) : # Creating a for loop from 1 till the number plus 1 to avoid exclusion of the input number
    sum += i
    product *= i

print('The sum of all integers from 0 to %d is %d' % (num,sum)) #Finding the printing the sum from 1 till the input number + 1
print('The sum of all integers from 1 to %d is %d' % (num,product)) #Finding the printing the product from 1 till the input number + 1 
    