#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:53:27 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 10b Act 1
# Date: 10/29/2020

import numpy as np
import matplotlib.pyplot as plt

#Define a function for Matrix multiplication to get the new point
def matrixmultiply(pV,MM):
    new_Point = MM @ pV
    return new_Point
    

#Create a 2D Point (x,y);(can be represented as vector)
point_V = np.array([[1],[0]])

#Create 2 x 2 matrix
matrix = np.array([[1.00583,-0.087156],[0.087156,1.00583]])

#Create array of x-values and y-values
x = np.array(point_V[0][0])
y = np.array(point_V[1][0])

#Initialize a new point as an iterator throughout the for loop
new_Point = matrixmultiply(point_V, matrix)

#Compute product of M with v to plot the points 250 times
for i in range(250):
    new_Point = matrixmultiply(new_Point,matrix)
    x = np.append(x,new_Point[0][0])
    y = np.append(y,new_Point[1][0])

#Plot the x-values and y-values and draw a red line
point = plt.plot(x,y,'g')

plt.xlabel('x-values')#Labeling the x-axis
plt.ylabel('y-values')#Labeling the y-axis
plt.title('Plot Matrix Multiplication - Spiral (Trace out)')#Create a title for the graph






