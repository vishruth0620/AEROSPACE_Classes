#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 08:15:11 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 12a Activity 1
# Date: 11/9/2020

import numpy as np 
import matplotlib.pyplot as plt
        
def converttoint(list_Coeff):#Define a function to convert the list of string coefficients inputted to a list of integer coefficients 
    
    """
    :param list_Coeff: list
    
    """


    new_List = []
    for i in range(len(list_Coeff)):
        new_List.append(int(list_Coeff[i]))
        
    return new_List

def derivative(list_Coeff):#Define a function to convert the list of string coefficients inputted to a list of integer coefficients, but this derivative list has 1 less element
    
    """
    :param list_Coeff: list
    """
    
    
    
    new_Coefficients = []
    for i in range(len(list_Coeff)-1):
        new_Coefficients.append((list_Coeff[i] * (len(list_Coeff) - i - 1))) #Computes the derivative of the orignal function list
    
    return new_Coefficients

def findmaxima_minima(y_Val):#Define a function to find maxima and minima using the y-values
    
    """
    :param y_Val: list
    """
    
    
    
    maxima = 0
    minima = 0
    for i in range(1,len(y_Val) - 1):
        if((y_Val[i] > y_Val[i-1]) and (y_Val[i] > y_Val[i+1])):#Find the local maxima
            maxima = i
        
        if((y_Val[i] < y_Val[i-1]) and (y_Val[i] < y_Val[i+1])):#Find the local minima
            minima = i
    
    return maxima, minima

def plotmaxima_minima(maxima,minima,x_Val,y_Val,color):#Define a function to plot the local maxima and minima points
    
    """
    :param maxima: int
    :param minima: int
    :param maxima: list
    :param minima: list
    :param color: string
    """
    
    
    if (maxima > 0):#Check if the maxima is not 0
        plt.plot(x_Val[maxima],y_Val[maxima],color)#Plot the maxima points
    if (minima > 0):#Check if minima is not 0
        plt.plot(x_Val[minima],y_Val[minima],color)#Plot the minima points




""" Main Program """ 

list_Coefficients = input('Enter the coefficients: ').split()#Input aribitrary amount of coefficients and will split them up into a list
original_List = converttoint(list_Coefficients)#Call the converttolistfunction to get orignal list of integer coefficients

original_Equation = np.poly1d(original_List)#Create a function from numpy class using the original function list
first_Derivative_Equation = np.polyder(original_Equation)#Get a first derivative equation using the original equation
second_Derivative_Equation = np.polyder(first_Derivative_Equation)#Get a second derivative equation using the first derivative equation

plt.figure()#Create a new figure
plt.axhline(color = 'black')#Create a x-axis
plt.axvline(color = 'black')#Create a y-axis
#Label x, y and the title of the graph
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plots of f(x),f\'(x),f\'\'(x) with local max and min')

x_Values = np.linspace(-5,5,70)#Create x-values from -5 to 5

y_Values = original_Equation(x_Values)#Set y-values to the original Equation of x-values
original_line,= plt.plot(x_Values,y_Values,'orange',linewidth = 3.0,label = 'f(x)')#Create the original function line
max_Index , min_Index = findmaxima_minima(y_Values)#Call the method findmaxima_minima to max and min index
plotmaxima_minima(max_Index, min_Index, x_Values, y_Values,'ko')#Call the plotmaxima_minima method


y_Values = first_Derivative_Equation(x_Values)#Set y-values to the first derivative equation of x-values
first_DerivativeLine,= plt.plot(x_Values,first_Derivative_Equation(x_Values),'r--',label = 'f\'(x)')#Create a first derivative equation line
max_Index , min_Index = findmaxima_minima(y_Values)#Call the method findmaxima_minima to max and min index
plotmaxima_minima(max_Index, min_Index, x_Values, y_Values,'bo')#Call the plotmaxima_minima method

second_DerivativeLine,= plt.plot(x_Values,second_Derivative_Equation(x_Values),'g:',linewidth = 2,label = 'f\"(x)')#Create a second derivative equation line

plt.legend(handles = [original_line,first_DerivativeLine,second_DerivativeLine],loc = 'upper left')#Create a legend for the three function lines
plt.show()



