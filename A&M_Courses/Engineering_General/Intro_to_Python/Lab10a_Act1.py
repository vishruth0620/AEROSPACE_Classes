#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 22:24:16 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Lilana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 10a Act 1
# Date: 10/26/2020

#“As a team, we have gone through all required sections of the tutorial,
#and each team member understands the material.”

import numpy as np

#Creating and Printing matrice A of 3 x 4
matrice_A = np.random.randint(10,size = (3,4))
print(matrice_A,'\n')

#Creating and Printing matrice B of 4 x @
matrice_B = np.random.randint(10,size = (4,2))
print(matrice_B,'\n')


#Creating and Printing matrice C of 2 x 3
matrice_C = np.random.randint(10,size = (2,3))
print(matrice_C,'\n')

#Creating and Printing matrice D of 3 x 1
matrice_D = np.random.randint(10,size = (3,1))
print(matrice_D,'\n')

#Creating and Printing the matrix multiplication of matrices A, B and C
product_E = matrice_A @ matrice_B @ matrice_C
print(product_E,'\n')

#Transposing and Printing of matrice E
transpose_E = product_E.T
print(transpose_E,'\n')

#Solving the linear system and Printing the answer to x variable
linear_system_X = np.linalg.solve(product_E,matrice_D)
np.set_printoptions(suppress = True,formatter = {'float_kind': '{:0.2f}'.format})
print(linear_system_X)