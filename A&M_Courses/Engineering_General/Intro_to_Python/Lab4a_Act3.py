#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 09:04:24 2020

@author: vishruth
"""
# Teammate Names: Hunter Spier, Liliano Salgado, Michael Camacho, Vishruth Balaji
# Assignment Lab 4a Activity 3
# Section: ENGR 102-451
# Date: September 9, 2020

########## Part A ##########
#Part A will ask for the user to enter True or False to assign a value of true or false to a,b,c.
#Using if and elif blocks, I will assign a boolean value to the input.

a = input('Enter True (True, T or t) or False (False, F or f) for a: ')
b = input('Enter True or False for b:  ')
c = input('Enter True or False for c:  ')


if (a == 'True' or a == 'T' or a== 't') :
    a = True

elif (a == 'False' or a == 'F' or a== 'f') :
     a = False
     
else :
    print("Value doesn't satisfy for variable a.")


if (b == 'True' or b == 'T' or b == 't') :
    b = True
    

elif (b == 'False' or b == 'F' or b == 'f') :
    b = False

else :
    print("Value doesn't satisfy for variable b.")
   

if (c == 'True' or c == 'T' or c == 't') :
    c = True   

elif (c == 'False' or c == 'F' or c == 'f') :
    c = False

else :
    print("Value doesn't satisfy for variable c.")
    
########## Part B ##########  
#Evaluate the boolean expressions using the
#operators and & or for variables a, b and c

boolean_test_1 = (a) and (b) and (c)
boolean_test_2 = (a) or (b) or (c)
print('')
print(boolean_test_1)
print(boolean_test_2)

########## Part C ##########   
#Evaluate the boolean expressions using the
#operators XOR & Odd Number for variables a, b and c
boolean_test_XOR = (a and not b) or (not a and b)
print(boolean_test_XOR)

boolean_test_OddNumber = (a and c) or (b and not b)
print(boolean_test_OddNumber)
