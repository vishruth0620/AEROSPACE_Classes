#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 00:25:03 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 9b Activity 3
# Date: 10/21/2020

import math
#Define a method to find the number of month corresponding to the parameter month
def find_month(month):
    list_Months = ['January','February','March','April','May','June','July','August','September','October','Novemeber','December']#Create of list of months
    for i in range(len(list_Months)):#Iterate through each element using for loop
        if(list_Months[i] == month):#Check if the element number satisfied with parameter
            return i + 1#Return month number

file = open('WeatherData.csv','r')#Open the WeatherData.csv file for reading
file.readline()#Forget the header
max_Temp = 0#Set a variable for maximum temperature
min_Temp = 999#Set a variable for minimum temperature
counter = 0#Initialize a counter
total_Precipitation = 0#Initialize the total precipitation
for weather_Data in file:#Look through each line using for lope in the file
    list_Details = weather_Data.split(',')#Separate each number in the line using split method
    if(int(list_Details[1]) > max_Temp):#Check to find maximum temperature
        max_Temp = int(list_Details[1])
    if(int(list_Details[3]) < min_Temp):#Check to find minimum temperature
        min_Temp = int(list_Details[3])
    
    total_Precipitation += float(list_Details[len(list_Details)-1])#Sum up total Precipitation on last column of the file
    counter += 1#increment by 1 for the denominator

print('3-year maximum temperature: {:d} F'.format(max_Temp))#Print out the maximum temperature
print('3-year minimum temperature: {:d} F'.format(min_Temp))#Print out the minimum temperature
print('3-year maximum temperature: {:.2f} inches\n'.format(total_Precipitation / counter))#Average the total precipitation
file.close()#Close the file to prevent malfunction

month = input('Enter a month: ')#Input a variable month as string
year = int(input('Enter a year: '))#Input a variable year as integer
print()

print('For {:s} {:d}:'.format(month,year))#Format the header 

file = open('WeatherData.csv','r')#Open the WeatherData.csv file again for reading
#Variables used for the 4 computations
total_low_Temperature = 0
counter_Temperature = 0
counter_less_than_75 = 0
total_Precipitation = 0
list_Precipitation = []#Create a list for third computation
month_Index = find_month(month)#Find the number of the month that was inputted
for i in range(1,32):#Range days from 1 to 32 using a for loop
    date_Value = str(month_Index) + '/' + str(i) + '/' + str(year)#Set a variable date_Value as a string to format the date
    for weather_Data in file:#Looking through each line in the file
        list_Details = weather_Data.split(',')#Separate each number in the line using split method
        
        if(date_Value == list_Details[0]):#Check if the date_Value is there in the first column for the reading file
            total_low_Temperature += int(list_Details[3])#Compute the 1st calculation by summing up all the low temperatures column
            counter_Temperature += 1#Increment counter by 1/used for all three computations    
            
            if(int(list_Details[8]) < 75):#Check if each value the Average Humidity Column is less than 75
                counter_less_than_75 += 1#Increment counter by 1
           
            total_Precipitation += float(list_Details[len(list_Details)-1])#Sum the preciptation column on the file
            
            list_Precipitation.append(float(list_Details[len(list_Details)-1]))#Append the daily precipitations for the standard deviation(4th computation)
            break
#Close file to prevent malfunctions
file.close()

print('Average low temperature: {:.2f} F'.format(total_low_Temperature/counter_Temperature))#Print the average of the low temperatures
print('Percentage of days with average humidity below 75%: {:.2f}%'.format(counter_less_than_75/counter_Temperature * 100))# Print the percentages of the average humidities less than 75

mean_Precipitaton = total_Precipitation / counter_Temperature #Calculate mean Precipitation
print('Mean daily precipitation: {:.4f} inches'.format(mean_Precipitaton))#Print the mean Precipitation

total_std_deviation = 0.0#Initialize a standard deviation variable to 0.0 as a float

for pr in list_Precipitation:#Iterate through each daily precipitation value in the list_Precipitations list
    total_std_deviation += math.pow(pr - mean_Precipitaton, 2)#Compute and sum of the total standard deviation

print('Standard deviation of daily precipitation: {:.4f} inches'.format(total_std_deviation / counter_Temperature))#Print the actual standard deviation of daily temperatures
    