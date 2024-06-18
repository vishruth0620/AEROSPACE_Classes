#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:28:52 2020

@author: vishruth
"""
# 	     By submitting this assignment I agree to the following
#          “Aggies do not, lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
#Name			Vishruth Balaji, Hunter Spier, Michael Camacho, Liliana Salgado
#Section		501
#Assignment		Lab9a_read
#Date			10/19/2020

file = input('Enter the filename: ')#Input the user a file name to read

f = open(file, 'r')#Open the file inputted

for line in f: #Read each line in the file
    if '10 MPa Data' in line:#Check if line equals '10 MPa Data' to print a new blank line for separation
        print()
    list_Values = line.split(',')#Separating the line into a list
    for value in list_Values:#Iterate through each value in the list
        print('{:>11}'.format(value), end = '')#Print the line with 11 spaces to the right
    
f.close()
        
        
        