#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:16:36 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 11b Activity 1c
# Date: 11/5/2020


def partc(full_Na,ad,ci,sta,zip_c):#Define a function partc that takes parameters full name, address, city, state and zipcode
    
    return '\n{:s}\n{:s}\n{:s}, {:s} {:d}'.format(full_Na,ad,ci,sta,zip_c) #Return the string as a mailing label


## Main Function ##
full_Name = input('Enter your full name (Last, First Middle Initial): ')#Input a full name 
address = input('Enter your address: ')#Input an address
city = input('Enter the city that you live in: ')#Input a city
state = input('Enter the state that you live in (use initials): ')#Input a state
zip_Code = int(input('Enter your zip code: '))#Input a zipcode

print(partc(full_Name,address,city,state,zip_Code))#Call the funtion partc and Print it out