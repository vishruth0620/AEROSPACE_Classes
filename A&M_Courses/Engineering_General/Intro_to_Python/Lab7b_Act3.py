#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 18:55:52 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Michael Camacho, Liliana Salgado
# Course Header: Eng 102-451
# Assignment: Lab 7b Activity 3
# Date: 10/1/2020

### Part A ###

#Create a list that enter values in the same row
#Initialize a list called original_List
values = input('Enter values for list: ').split()
original_List = []

#Using a for loop, add values from the variable values to list original_List as float numbers
for value in values:
    original_List.append(float(value))

#Create a new list called sorted_List
sorted_List = []

#Use a while loop to find the first minimum value, 
#then remove the minimum value for the original_List 
#and add to the sorted_List, so it the sorted list goes from minimum to maximum 
while len(original_List) > 0:
    minimum_Value = min(original_List)
    sorted_List.append(minimum_Value)
    original_List.remove(minimum_Value)

#Output the minimum and maximum value of the sorted list to the console
#print(sorted_List)
print('The minimum value is %.1f' % (sorted_List[0]))
print('The maximum value is %.1f' % (sorted_List[len(sorted_List) - 1]))


### Part B ###

#If the length of the list is an odd number, then average the value from the item that's 
#half of the length using integer division and the value before to get the median
if(len(sorted_List) % 2 == 0):
    item = len(sorted_List) // 2
    median = float(sorted_List[item] + sorted_List[item - 1]) / 2.0

#If the length of list is an even number, then find the item value by dividng the
#length of the list by 2 using integer division to find the median 
else:
    item = len(sorted_List) // 2
    median = sorted_List[item]

#Output the median of the sorted_list to the console
print('The median is %.1f' % (median))
