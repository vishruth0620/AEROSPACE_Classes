#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:43:10 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 11b Activity 1f
# Date: 11/5/2020

def partf(list_Time,list_Distance):#Define a function partf taking parameters list_Time and list_Distances
    list_Average_Velocity = []#Create an empty list of average velocities
    average_Velocity = 0.0 # Creating an average velocity computation variable
    for i in range(len(list_Time) - 1):#Use a for loop to range of len of list times - 1            
        average_Velocity = (list_Distance[i+1] - list_Distance[i]) / (list_Time[i+1] - list_Time[i])#Compute average velocity
        list_Average_Velocity.append(average_Velocity)#Append the average velocity to the list of average veloctities
    
    return list_Average_Velocity#Return the list of average velocities



## Main Function ##
list_Times = [1,2,3,4,5,6,7,8]#Listing Times in increaing order

list_Distances = [25,36,48,74,82,56,90,117]#Test Case 1
print('Average Velocity:',partf(list_Times,list_Distances))#Print Average Velocity of Test Case 1
list_Distances2 = [134,54,75,89,98,56,145,136]#Test Case 2
print('Average Velocity:',partf(list_Times,list_Distances2))#Print Average Velocity of Test Case 2
list_Distances3 = [144,117,24,67,95,13,210,398]#Test Case 3
print('Average Velocity:',partf(list_Times,list_Distances3))#Print Average Velocity of Test Case 3