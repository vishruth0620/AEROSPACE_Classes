#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:17:12 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Michael Camacho, Liliana Salgado
# Course Header: Eng 102-451
# Assignment: Lab 7b Activity 1
# Date: 9/30/2020

import math

#Creating inputs for decimal value components for Vector A using an input statement
#Initialize an empty list to variable vector_A
vector_components_A = input('Enter the x, y and z components for vector A: ').split()
vector_A = []

#Creating inputs for decimal value components for Vector A using an input statement
#Initialize an empty list to variable vector_B
vector_components_B = input('Enter the x, y and z components for vector B: ').split()
vector_B = []

#Using a for loop,
#Add values from the variable vector_components_A to list vector_A
#Calculate the inner part for solving magnitude of vector A
inner_Vector_A = 0
for item in vector_components_A:
    vector_A.append(float(item))
    inner_Vector_A += math.pow(float(item),2)

#Using a for loop,
#Add values from the variable vector_components_B to list vector_B
#Calculate the inner part for solving magnitude of vector B
inner_Vector_B = 0
for item in vector_components_B:
    vector_B.append(float(item))
    inner_Vector_B += math.pow(float(item),2)
    
#Check if the length of vector A is equal to vector B
if (len(vector_A) == len(vector_B)):
    
    #Calculate the magnitude for vector A by square rooting the inner_Vector_A variable
    #Output the magnitude for vector A to the console
    magnitude_Vector_A = math.sqrt(inner_Vector_A)
    print('The magnitude of vector A is %.5f' % (magnitude_Vector_A))
    
    #Calculate the magnitude for vector B by square rooting the inner_Vector_B variable
    #Output the magnitude for vector A to the console
    magnitude_Vector_B = math.sqrt(inner_Vector_B)
    print('The magnitude of vector B is %.5f' % (magnitude_Vector_B))
    
    #Initalize new lists for the vector_Sum and vector_Difference
    vector_Sum = []
    vector_Difference = []
    
    #Initialize the dot product to 0.0 as a floating.point number
    dot_Product = 0.0
    
    #Using a for loop,
    #Add values from each element of both vector_A and vector_B lists and add the calculate value to vector_Sum list 
    #Subtract values from each element of both vector_A and vector_B lists and add the calculate value to vector_Difference list
    #Calculate the inner part for solving magnitude of vector B
    #Calculate the dot_product by multiplying two values from each element in the two lists and adding them together
    for i in range(len(vector_A)):
        vector_Sum.append(vector_A[i] + vector_B[i])
        vector_Difference.append(vector_A[i] - vector_B[i])
        dot_Product += (vector_A[i] * vector_B[i])
        
    #Output the vector_Sum list to the console
    #Output the vector_Difference list to the console   
    #Output the dot_Product list to the console   
    print('A + B is',vector_Sum)
    print('A - B is',vector_Difference)
    print('The dot product is',dot_Product)

#If the lengths of both vector_A and vector_B don't match, then they don't match and would need to try again
else:
    print('The vector lengths don\'t match.')


    