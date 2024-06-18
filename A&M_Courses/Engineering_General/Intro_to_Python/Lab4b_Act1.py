#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:28:06 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 4b Activity 2
# Date: 9/9/2020


num_1 = float(input('Enter number 1: ')) #Inputting number 1
num_2 = float(input('Enter number 2: ')) #Inputting number 2
num_3 = float(input('Enter number 3: ')) #Inputting number 3

#Checking to see which number out of the three is the largest and printing it out
if ((num_1 > num_2) and (num_1 > num_3)) :
    print('\nThe largest number is',num_1)
    
elif ((num_2 > num_1) and (num_2 > num_3)) :
    print('\nThe largest number is',num_2)

elif ((num_3 > num_1) and (num_3 > num_2)) :
    print('\nThe largest number is',num_3)
