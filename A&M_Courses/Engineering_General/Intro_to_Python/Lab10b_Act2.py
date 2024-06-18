#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:05:44 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 10b Act 2
# Date: 10/29/2020

import numpy as np
import matplotlib.pyplot as plt

#Defining the method of getting the month based on the date
def get_month(d):
    list_Date = d.split('/')#Splitting the date
    month = int(list_Date[0]) - 1 #Getting the month as an integer
    return month #Returning the month

#Defining the method of calculating average temperature using the list of temperatures
def calculate_avg_temperature(list_Temp):
    sum_avg_Temps = 0 #Initializing a sum of avg temps to 0
    for i in range(len(list_Temp)): #Go throught the list of temperatures
        sum_avg_Temps += list_Temp[i] #Adding it to sum_avg_Temps
    
    return float(sum_avg_Temps / len(list_Temp)) #Finding the avg of the Temperatures

#Defining a method of getting bins with no parameter
def get_bins():
    bins = []
    i = 0.0
    while (i < 9.0):
        bins.append(i)
        i += 0.1
    
    return bins
    

## Part A ##

#Read in the file from Lab 9b Act 3
file = open('WeatherData.csv','r')#Open the WeatherData.csv file for reading

file.readline()#Forget the header
days = []#Cretae a list of days
list_avg_Temperatures = []#Create an empty list of avg temperatures
list_avg_Pressures = []#Create an empty list of avg pressures
list_Precipitation = []#Create an empty list of precipitation
list_avg_DewPoint = []#Create an empty list of avg dew points
num_Days = 0 #Create counter of num days to 0
array_num_P_days = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#Create array num of P days
for weather_Data in file:#Look through each line using for loop in the file
    list_Details = weather_Data.split(',')#Separate each number in the line using split method
    num_Days += 1#Add counter b 1
    days = np.append(days,num_Days)#Append num_Days to days list
    avg_temp = float(list_Details[2]) #Taking the 3rd element of list-Details to variable avg_temp
    list_avg_Temperatures = np.append(list_avg_Temperatures,avg_temp)#Append the avg temperature to list avg_temperatures
    avg_pressure = float(list_Details[11])#Taking the element 11 of list-Details to variable avg_temp
    list_avg_Pressures = np.append(list_avg_Pressures,avg_pressure)
    precipitation = float(list_Details[13])#Taking the 14th element of list-Details to variable avg_temp
    
    if (precipitation > 0):#For part B, it shows no precipitation values for precipitation = 0
        list_Precipitation = np.append(list_Precipitation,precipitation)#Append it to list_Precipitation
    
    avg_DewPoint = int(list_Details[5])#Taking the 6th element of list-Details to variable avg_temp
    list_avg_DewPoint = np.append(list_avg_DewPoint,avg_DewPoint)#Appending it to list average Dew Points


plt.title('Average Temperature and Pressure for Data Range')#Titling the graph
plt.axis([-50, 1201, 25, 91])#Creating a x and y-range for the left y-side
plt.xlabel('Date')#Labeling the x-axis
line_1,= plt.plot(days,list_avg_Temperatures,'r', label = 'T avg')#plotting a line 1
plt.ylabel('Average Temperature, F')#Labeling the left y-axis of the graph
plt.twinx()#Creating a right side y-label
plt.axis([-50, 1201, 29.5, 30.6])#Creating the y-range for the right y-side
line_2, = plt.plot(days,list_avg_Pressures,'b', label = 'P avg')#plotting a line 2
plt.ylabel('Average Pressure, inHg')#Labeling the right y-axis of the graph

plt.legend(handles = [line_1,line_2],loc = 'best')#Creating a legend
plt.show()#Showing the graph


## Part B ##

plt.xticks(np.arange(0,9,1))#Creating x intervals on the graph
plt.hist(list_Precipitation,get_bins(),rwidth = 0.95, facecolor='b', alpha=1.0)#Plotting the histogram
plt.title('Histogram of Precipiation')#Titling the Grsph
plt.xlabel('Precipitation, in')#Labeling the x-axis
plt.ylabel('Number of Days')#Labeling the y-axis
plt.show()#Showing the graph


## Part C ##
plt.scatter(list_avg_Temperatures,list_avg_DewPoint,c = 'black',s = 10)#Plotting a scatter graph
plt.title('Dew Point vs Temperature')#Titling the graph
plt.xlabel('Average Temperature,F')#Labeling the x-axis
plt.ylabel('Average Dew Point,F')#Labeling the y-axis
plt.show()#Show the graph
file.close()#Close the file to prevent malfunction


## Part D ##

file = open('WeatherData.csv','r')#Open the WeatherData.csv file for reading
file.readline()#Forget the header
array_Months = [[],[],[],[],[],[],[],[],[],[],[],[]]#Creating an array months
array_high_Temp = [0,0,0,0,0,0,0,0,0,0,0,0]
array_low_Temp = [999,999,999,999,999,999,999,999,999,999,999,999]
array_avg_Temp = [0,0,0,0,0,0,0,0,0,0,0,0]
for weather_Data in file:#Look through each line using for loop in the file
    list_Details = weather_Data.split(',')#Separate each number in the line using split method
    month = get_month(list_Details[0])#Getting the 1st element from list_Details
    avg_temp = float(list_Details[2]) #Getting the 3rd element from list_Details
    array_Months[month].append(avg_temp)
    if(int(list_Details[1]) > array_high_Temp[month]):#Check to find maximum temperature
        array_high_Temp[month] = int(list_Details[1])#Setting the maximum temperature to arrra of high temperatures in the corresponding month
        
    if(int(list_Details[3]) < array_low_Temp[month]):#Check to find minimum temperature
        array_low_Temp[month] = int(list_Details[3])#Setting the minimum temperature to arrra of high temperatures in the corresponding month

for i in range(12): #Create a for loop from 0 to 11
    array_avg_Temp[i] = calculate_avg_temperature(array_Months[i])#Use the calculate avg temperatue function and change the value in list avg_temp

x_values = np.arange(1,13,1)#Creating a range from 1 to 13
plt.xticks(x_values)#Creating x-value marks on the graph
high_temp_Line, = plt.plot(x_values,array_high_Temp,'r',label = 'High T')#Plotting the High Temperature Line
low_temp_Line, = plt.plot(x_values,array_low_Temp,'b',label = 'Low T')#Plotting the Low Temperature Line
plt.bar(x_values,array_avg_Temp, facecolor='y',alpha = 1)#Plotting the bar into he graph

plt.legend(handles = [high_temp_Line,low_temp_Line],loc = 'upper left')#Creating a legend at upper left corner
plt.title('Average Temperature by Month')#Titling the graph
plt.xlabel('Month')#Labeling the x-axis
plt.ylabel('Average Temperature, F')#Labeling the y-axis
plt.show()#Show the graph
file.close()#Close the file to prevent malfunction