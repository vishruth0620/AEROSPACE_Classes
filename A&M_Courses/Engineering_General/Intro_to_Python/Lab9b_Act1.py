#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:24:18 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 9b Activity 1
# Date: 10/19/2020

#Method to convert from Celcius to Fahrenheit using Celcius as parameter
def celsiustofahrenheit(c):
    f = (1.8) * c + 32.0 #Formula for converting Celcius to Fahrenheit
    return "{:.2f}".format(f) #Return the Fahrenheit value to 2 decimal places

file_1 = open('Celsius.txt','r')#Open the Celcius.txt file for reading
file_2 = open('Fahrenheit.txt','w')#Open the Fahrenheit.txt file for writing
for celsius in file_1:#Reading each line from Celcius.txt
    file_2.write(celsiustofahrenheit(float(celsius)).rjust(10))#Compute through the celciustoFahrenheit method and 
    #right_justify it with 10 spaces/ Write it to the Fahrenheit.txt file
    
    file_2.write('\n')

#Close both the files to prevent malfunction
file_1.close()
file_2.close()
    
    
    
    