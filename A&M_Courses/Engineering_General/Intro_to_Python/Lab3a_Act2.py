#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 07:41:48 2020

@author: vishruth
"""
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 3a Activity 2
# Date: 9/2/2020

user_Name = 'Name'
user_Birthday = 'Birthday'

# Inputting names and their corresponding birthdays to the name and birthday variables
name1 = str(input('User 1, please enter your name: '))
birthday1 = str(input('Enter the first birthday (mm/dd/yyyy) corresponding with Name 1: ')) #mm/dd/yyyy

name2 = str(input('User 2, please enter your name: '))
birthday2 = str(input('Enter the second birthday (mm/dd/yyyy) corresponding with Name 2: ')) #mm/dd/yyyy

name3 = str(input('User 3, please enter your name: '))
birthday3 = str(input('Enter the third birthday (mm/dd/yyyy) corresponding with Name 3: ')) #mm/dd/yyyy

name4 = str(input('User 4, please enter your name: '))
birthday4 = str(input('Enter the fourth birthday (mm/dd/yyyy) corresponding with Name 4: ')) #mm/dd/yyyy

#Printing out the names of the inputs and it birthdays in correspondence with their names
print('\n\n')

print('%20s %20s' % (user_Name, user_Birthday))
print('%20s %20s' % ('-----','--------'))
print ('%20s %20s' % (name1, birthday1))
print ('%20s %20s' % (name2, birthday2))
print ('%20s %20s' % (name3, birthday3))
print ('%20s %20s' % (name4, birthday4))
