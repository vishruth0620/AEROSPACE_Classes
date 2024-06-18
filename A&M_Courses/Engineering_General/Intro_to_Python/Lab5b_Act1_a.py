#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:00:10 2020

@author: vishruth
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 5b Activity 1a
# Date: 9/14/2020

counter = 0; #Setting a counter of number of Iterations in the loop
num = int(input('Enter a positive integer to compute the Collatz sequence: ')) #Input an integer from the user
print('Here is the Collatz sequence starting at {}: '.format(num)) #Printing the starting statement for Collatz Sequence
print('%d'% (num), end = '') #String Formatting

while num != 1 : #Setting a while loop for creating numbers in a Collatz sequence until it hits 1.
    if (num % 2 == 0) : #Setting an if statement to check whether the variable num is even
        num /= 2 #Divide the number by 2 to get a new number
        print(', %d' % (num), end = '') #Print the variable number as a string format
    
    elif (num % 2 != 0) : #Setting an elif statement to check whether the variable num is odd
        num = (3 * num) + 1 #USe the form 3n +1 and plug in number for n to get new number
        print(', %d'% (num), end = '') #Print the variable number as a string format
    
    counter += 1

 
print('\nIt took {:d} iterations to reach 1.'.format(counter)) #Printting out the number of iterations of the while loop until variable num is 1