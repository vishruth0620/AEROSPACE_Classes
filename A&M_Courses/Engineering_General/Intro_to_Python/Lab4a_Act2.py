#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:24:31 2020

@author: vishruth
"""
# Teammate Names: Hunter Spier, Liliano Salgado, Michael Camacho, Vishruth Balaji
# Assignment Lab 4a Activity 2
# Section: ENGR 102-451
# Date: September 7, 2020

#Inputting variables of Number of Hours when car is parked
parking_charge_Fee = 0
num_parked_Hours = float(input('How long was the vehicle in the garage (hours)? '))

#Iterating through the if statements to find the Parking Charge Fee
if num_parked_Hours < 0:
    parking_charge_Fee += 36
    num_parked_Hours = abs(num_parked_Hours)
if num_parked_Hours == 0:
    parking_charge_Fee = 0
else:
    while num_parked_Hours > 0:
        if num_parked_Hours >= 24:
            num_parked_Hours -= 24
            parking_charge_Fee += 24
        elif 22 <= num_parked_Hours < 24:
            num_parked_Hours -= num_parked_Hours
            parking_charge_Fee += 24
        elif num_parked_Hours < 22:
            if num_parked_Hours <= 2:
               num_parked_Hours -= 2
               parking_charge_Fee += 4
            elif 2 < num_parked_Hours <= 4:
                num_parked_Hours -= 2
                parking_charge_Fee +=3
            elif num_parked_Hours > 4:
                num_parked_Hours -= 1
                parking_charge_Fee += 1
#Printing out the Parking Charge Fee based on the number of hours
#parked in the garage
print('The charge is ${}.'.format(parking_charge_Fee))
