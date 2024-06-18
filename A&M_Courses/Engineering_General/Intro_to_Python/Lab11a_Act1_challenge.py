#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:05:25 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 11a Challenge
# Date: 11/7/2020

import math as mp

def F(x_Val):#Define a F function with parameter of an x value
    
    y_Value = mp.log(1.0 / (x_Val ** 2 + 1)) * mp.sin(x_Val)#Create the F equation and use math class for different functions
    return y_Value #Return the y value of function F at that x-value

def G(x_Val):#Define a G function with parameter of an x value
    
    y_Value = mp.sin(x_Val) + 2.0#Create the G equation and use math class for different functions
    return y_Value#Return the y value of function G at that x-value

def H(x_Val):#Define a H function with parameter of an x value
    
    y_Value = mp.pow(x_Val, 3) + 4.0 * (x_Val ** 2) + 45.0#Create the H equation and use math class for different functions 
    return y_Value#Return the y value of function H at that x-value

def J(x_Val):#Define a J function with parameter of an x value
    
    y_Value = abs(x_Val ** 2) + 23.0#Create the J equation and use math class for different functions
    return y_Value#Return the y value of function J at that x-value

def K(x_Val):#Define a K function with parameter of an x value
    
    y_Value = x_Val ** 2 - 9.0#Create the K equation and use math class for different functions
    return y_Value#Return the y value of function K at that x-value



def deriv(x,Func):#Defining the derivative passing in the x_Value and the Function
    a = 0.001 #Assigning a to 0.001
    return float((Func(x+a) - Func(x)) / a)#Returning the derivative of the function using definition of a derivative at that x_Val

def newton_step(xi,Func):#Define a newton function that passes x as a parameter
    x_i1 = xi - (Func(xi) / deriv(xi,Func))#Create the formula of the newton step given at the top of the document
    return x_i1#Return the next stepn approximation root

def newton(x0,Func):#Define a function called newton that passes an x parameter
    
    real_Root = False #Setting boolean variable real_Root to false
    pre_Root = newton_step(x0,Func)#Create the pre root by calling the newton step method
    if(Func(pre_Root) == 0.0):#Checking if the y value of the pre root in function is equal to zero
        real_Root = True #Set real root equal to true
    
    l_Roots = [x0,pre_Root]#Create a list called l_Roots with the x parameter and the next step approximation

    while (True):#Set true as condition in while loop
        
        cur_Root = newton_step(pre_Root,Func)#Get current root by calling newton step for the next approximation
        
        if(Func(cur_Root) == 0.0):#Checking if the y value of the cur_root root in function is equal to zero
             real_Root = True #Set real root equal to true
    
        l_Roots.append(cur_Root)#Append the current root to the list
        
        if((pre_Root - cur_Root) <= (10 ** -6)):#Check if the difference of previous root and current root is less than the tolerance
            break #If true, break the for loop
        
        pre_Root = cur_Root#Set the current root to pre_root
        
        
    if(real_Root == False):#Cheking if the boolean real_root is false
       print('\nThere are no real roots for the function.')#Print the statement
   

    return l_Roots#Return the list of real roots


initial_Guess = float(input('Enter an initial guess for a root of f(x): '))#Input a initial guess number

print('\nThe root approximations for f(x) are: ')#Print starting line
list_Roots = newton(initial_Guess,F)#Call the newton method with the parameter of initial_Guess and F
print(' -> '.join('{:0.6f}'.format(val) for val in list_Roots))#Print the list of roots for Function F by spacing each value with a parameter


print('\nThe root approximations for g(x) are: ')#Print starting line
list_Roots = newton(initial_Guess,G)#Call the newton method with the parameter of initial_Guess and G
print(' -> '.join('{:0.6f}'.format(val) for val in list_Roots))#Print the list of roots for Function G by spacing each value with a parameter


print('\nThe root approximations for h(x) are: ')#Print starting line
list_Roots = newton(initial_Guess,H)#Call the newton method with the parameter of initial_Guess and H
print(' -> '.join('{:0.6f}'.format(val) for val in list_Roots))#Print the list of roots for Function H by spacing each value with a parameter


print('\nThe root approximations for j(x) are: ')#Print starting line
list_Roots = newton(initial_Guess,J)#Call the newton method with the parameter of initial_Guess and J
print(' -> '.join('{:0.6f}'.format(val) for val in list_Roots))#Print the list of roots for Function J by spacing each value with a parameter


print('\nThe root approximations for k(x) are: ')#Print starting line
list_Roots = newton(initial_Guess,K)#Call the newton method with the parameter of initial_Guess and K
print(' -> '.join('{:0.6f}'.format(val) for val in list_Roots))#Print the list of roots for Function K by spacing each value with a parameter
