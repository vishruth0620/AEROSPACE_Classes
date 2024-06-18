#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:21:03 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Michael Camacho, Liliana Salgado
# Course Header: Eng 102-451
# Assignment: Lab 7a Activity 2
# Date: 9/28/2020

import math

#### Part A ####

#Use the list from the separate python file that Dr. Lara sent
#Initialize the calculated variable sum_Grades to 0
gradeData = [69,99,73,59,67,65,52,99,57,58,67,88,72,69,41,74,53,90,63,66,92,54,61,59,48,71,83,89,100,69,66,39,48,41,99,68,52,78,77,73,40,65,77,87,96,44,54,60,89,72]
sum_Grades = 0

#Iterate each grade value from the list gradeData using a for loop
#Add every grade to the variable sum_Grades
for grade in gradeData:
    sum_Grades += grade

#Calculate the variable mean_Grades by dividing the variable sum_Grades by total number of grades in the list
mean_Grades = sum_Grades / len(gradeData)

#Output the mean of the list to the Console
print('The mean is %.2f' % (mean_Grades))


#### Part B ####

#Reuse the list gradeData for Part B
#Initialize the calculated variable sum_variance_Grade to 0
sum_variance_Grade = 0

#Iterate each grade value from the list gradeData using a for loop
#Power the difference of grade minus mean_Grades found in Part A to 2
#Then add it to variable sum_variance_Grade
for grade in gradeData:
    sum_variance_Grade += math.pow(grade - mean_Grades,2)

#Take the variable sum_variance_Grade and divide it by the length of the list, then squarer root the answer
#to find the standard deviation
standard_Deviation = math.sqrt(sum_variance_Grade / len(gradeData))

#Output the standard deviation to the Console
print('The standard deviation is %.4f' % (standard_Deviation))


#### Part C ####

#Reuse the list gradeData for Part C
#Set the minimum and maximum grades to the first element on the list gradeData
minimum_Grade = gradeData[0]
maximum_Grade = gradeData[0]

#Iterate each grade value from the list gradeData using a for loop
for grade in gradeData:
    
    #Finding a minimum grade and maximum grade out of the list gradeData using if-elif statement
    if(grade < minimum_Grade):
        minimum_Grade = grade
    
    elif(grade > maximum_Grade):
        maximum_Grade = grade

#Output the minimum grade and maximum grade in the Console
print('The min is %d' % (minimum_Grade))
print('The max is %d' % (maximum_Grade))