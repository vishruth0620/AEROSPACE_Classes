#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:47:25 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 11a Activity 1
# Date: 11/4/2020

import math as mp

def F(x_Val):#Define a function with parameter of an x value
    
    y_Value = mp.log(1.0 / (x_Val ** 2 + 1)) * mp.sin(x_Val) #Create the final submission equation and use math class for different functions
    return y_Value #Return the y value of the function at that x-value

def deriv(x):#Define a derivative that passes an x parameter
    a = 0.001 #Assigning a to 0.001
    return float((F(x+a) - F(x)) / a)#Returning the derivative of the function using definition of a derivative at that x_Val

def newton_step(xi):#Define a newton function that passes x as a parameter
    x_i1 = xi - (F(xi) / deriv(xi))#Create the formula of the newton step given at the top of the document
    return x_i1#Return the next stepn approximation root

def newton(x0):#Define a function called newton that passes an x parameter
    
    pre_Root = newton_step(x0) #Create the pre root by calling the newton step method
    l_Roots = [x0,pre_Root]#Create a list called l_Roots with the x parameter and the next step approximation
    
    while (True): #Set true as condition in while loop
        cur_Root = newton_step(pre_Root) #Get current root by calling newton step for the next approximation
        l_Roots.append(cur_Root)#Append the current root to the list
        if((pre_Root - cur_Root) <= (10 ** -6)):#Check if the difference of previous root and current root is less than the tolerance
            break #If true, break the for loop
        
        pre_Root = cur_Root#Set the current root to pre_root
        
    return l_Roots#Return the list of roots



initial_Guess = float(input('Enter an initial guess for a root of f(x): '))#Input a initial guess number

list_Roots = newton(initial_Guess)#Call the newton method with the parameter of initial_Guess

print('\nThe root approximations are: ')#Print starting line
print(' -> '.join('{:0.6f}'.format(val) for val in list_Roots))#Print the list of roots by spacing each value with a parameter
