#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:09:53 2020

@author: vishruth
"""
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 3a Activity 3
# Date: 9/2/2020


#Inputting eight variables of the Mad Lib 

#define variable gender with user input
gender = input('Enter the gender: ')
#define variable name with user input
name = input('Enter the first name of the person: ')
#define name_place with user input
name_Place = input('Enter the name of the place: ')
#define variable thing with user input
thing = input('Please enter the thing: ')
#define variable adjective with user input
adjective = input('Please enter an adjective: ')
#define variable verb with user input
verb = input('Please enter a verb: ')
#define variable num_years with user input
num_Years = int(input('Please enter the number of years: '))
#convert years into months, and store variable in num_years
num_Months = num_Years * 12
#define variable amount with user input
amount = str(input('Please enter a price: '))
#define variable name2 with user input
name2 = str(input('Please enter a second name: '))

#Printing out the Mad Lib story with the eight inputs included
print ('\n\nThere was once a %s whose name was %s in %s.\nThe %s this %s owned was so %s he could %s with it.\n%s spent all their %s months trying to earn the $%s to get more %s.\nThis %s was a special gift for %s, %s\'s best friend.' % (gender, name, name_Place, thing, gender, adjective, verb, name, num_Months, amount, thing, thing, name2, name))




