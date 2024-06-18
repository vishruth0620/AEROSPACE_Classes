#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:42:24 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Lilana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 10a Act 2
# Date: 10/28/2020

#“As a team, we have gone through all required sections of the tutorial,
#and each team member understands the material.”


import numpy as np
from numpy import sin,cos,pi
import matplotlib.pyplot as plt

## Part A ##

#Defining a function for the parabola equation using focal length and x values and return y values
def parabola(f,x):
    return 1/(4 * f) * (x ** 2)

#Titling the Graph 
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.title('Parabola Plots with Varying Focal Length')


x_Value = np.linspace(-2.0,2.0,50)#Giving a range of x-values from -2.0 to 2.0 with 50 samples
line, = plt.plot(x_Value,parabola(2,x_Value),color = 'green',linewidth = 2.0,label = 'f=2')#Plot (x,y) points with focal length 2; draw a green line of line width 2.0
line.set_antialiased(True)#Prevent jaggered lines

line_2, = plt.plot(x_Value,parabola(6,x_Value),color = 'orange',linewidth = 4.0,label = 'f=6')#Plot (x,y) points with focal length 6; draw a orange line of line width 4.0
line.set_antialiased(True)#Prevent jaggered lines

#Set a legend of labels f = 2 and f = 6 at the lower left corner of the graph
plt.legend(handles = [line,line_2],loc = 'lower left')

plt.show()


## Part B ##


#Define a cubic function to pass in the x-values and return y-values from the cubic function
def cubic(x):
    return (2 * (x ** 3)) + (3 * (x ** 2)) - (11 * (x)) - 6
    
#Titling the Graph 
plt.xlabel('x-values')
plt.ylabel('y values')
plt.title('Plot of Cubic Polynomial')

x_Value2 = np.arange(-4.,4.3,.34)#Use a range from the -4 to 4 with increment of 0.34
plt.plot(x_Value2,cubic(x_Value2),'*')#Plot (x,y) points using stars as the marker

plt.show()

## Part C ##


#Define a sine function to pass in the x-values and return y-values from the sine function
def sine_function(x):
    return sin(x)

#Define a cosine function to pass in the x-values and return y-values from the cosine function
def cosine_function(x):
    return cos(x)

#Titling the Graph
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.title('Plot of cos(x) and sin(x)')

x_Value3 = np.linspace(-2*pi,2*pi,50)#Giving a range of x-values from -2pi to 2pi with 50 samples
cos_line,= plt.plot(x_Value3,cosine_function(x_Value3),'magenta',label = 'cos(x)')#Plot (x,y) points and draw a magenta line
cos_line.set_antialiased(True)#Prevent jaggered lines

sin_line,= plt.plot(x_Value3,sine_function(x_Value3),'blue',label = 'sin(x)')#Plot (x,y) points and draw a blue line
sin_line.set_antialiased(True)#Prevent jaggered lines

#Set a legend of labels cos(x) and sin(x) at the lower left corner of the graph
plt.legend(handles = [cos_line,sin_line],loc = 'lower left')