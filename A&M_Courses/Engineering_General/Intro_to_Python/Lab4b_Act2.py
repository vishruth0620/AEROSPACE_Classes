#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:08:12 2020

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


widgets = 0 #Setting initial value of widgets to 0
days = int(input('Please enter a positive value for days: ')) #Inputting variable days
              
#Checking whether or not days is a negative number to print an invalid number
if (days <= 0) :
    print('\nYou entered an invalid number!')


else :
    
    initial_days = 1; #Setting variable initial days to 1 as a counter to iterate through if statements
    
    while (initial_days <= days and initial_days < 101) : #Having a while loop to find the number of widgets for 0 to 100
        
        if (initial_days > 60) : #If initial days is between 61 and 100
            widgets += (100 - initial_days)
    
        elif (initial_days > 10) : #If initial days is between 11 and 60
            widgets += 40
        
        else : #If initial days is between 1 and 10
            widgets += 10
    
        initial_days += 1
    
    print('\nThe total number of widgets produced on day {} is {}.'.format(days, widgets)) #Printing the number of widgets on that day number
        