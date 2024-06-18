#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:58:49 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 6A Activity 2
# Date: 9/21/2020

#Input Variables that tells information about the person
gender = input('Enter your sex (M/F): ') #M stand for male; F stands for female
age = int(input('Enter your age (years): '))
total_Cholesterol = int(input('Enter your total cholesterol (mg/dL): '))
is_Smoker = input('Do you smoke cigarettes (Y/N)? ')
HDL_Cholestrol = int(input('Enter your HDL cholesterol (mg/dL): '))
systolic_BP = int(input('Enter your systolic BP (mmHg): '))
is_Treated = input('Are you taking blood pressure medication (Y/N)? ')

#Check the gender (Male of Female) using the upper method
#Also to check switch case of male or female

gender = gender.upper()

is_Smoker = True if (is_Smoker.upper() == 'Y') else False

is_Treated = True if (is_Treated.upper() == 'Y') else False
  

#Initialize the variable sum_Points as a calculated variable
sum_Points = 0
    
    

#Compute points based on age using an if-elif statements
#Add the points to variable sum_Points
#Using single line if-statments to save lines on code

if (20<= age <= 34):
    sum_Points += -9 if (gender == 'M') else -7

elif(35 <= age <= 39):
    sum_Points += -4 if (gender == 'M') else -3

elif(40 <= age <= 44):
    sum_Points += 0
    
elif(45 <= age <= 49):
    sum_Points += 3
        
elif(50 <= age <= 54):
    sum_Points += 6
    
elif(55 <= age <= 59):
    sum_Points += 8

elif(60 <= age <= 64):
    sum_Points += 10
    
elif(65 <= age <= 69):
    sum_Points += 11 if (gender == 'M') else 12
        
elif(70 <= age <= 74):
    sum_Points += 12 if (gender == 'M') else 14

elif(75 <= age <= 79):
    sum_Points += 13 if (gender == 'M') else 16

  
#Compute points based on total cholesterol and age using an if-elif statements
#Add the points to variable sum_Points
#Using single line if-statments to save lines on code

if (total_Cholesterol < 160):
    sum_Points += 0
         
elif (160 <= total_Cholesterol <= 199):
        
        if(20 <= age <= 39):
            sum_Points += 4

        elif(40 <= age <= 49):
            sum_Points += 3
            
        elif(50 <= age <= 59):
            sum_Points += 2
        
        elif(60 <= age <= 69):
            sum_Points += 1
        
        elif(70 <= age <= 79):
            sum_Points += 0 if(gender == 'M') else 1

elif (200 <= total_Cholesterol <= 239):
        
        if(20 <= age <= 39):
            sum_Points += 7 if(gender == 'M') else 8

        elif(40 <= age <= 49):
            sum_Points += 5 if(gender == 'M') else 6
            
        elif(50 <= age <= 59):
            sum_Points += 3 if(gender == 'M') else 4
        
        elif(60 <= age <= 69):
            sum_Points += 1 if(gender == 'M') else 2
        
        elif(70 <= age <= 79):
            sum_Points += 0 if(gender == 'M') else 1                                 
    
elif (240 <= total_Cholesterol <= 279):
        
    if(20 <= age <= 39):
            sum_Points += 9 if(gender == 'M') else 11

    elif(40 <= age <= 49):
            sum_Points += 6 if(gender == 'M') else 8
            
    elif(50 <= age <= 59):
            sum_Points += 4 if(gender == 'M') else 5
        
    elif(60 <= age <= 69):
            sum_Points += 2 if(gender == 'M') else 3
        
    elif(70 <= age <= 79):
            sum_Points += 1 if(gender == 'M') else 2
    
elif (total_Cholesterol >= 280):
        
    if(20 <= age <= 39):
            sum_Points += 11 if(gender == 'M') else 13

    elif(40 <= age <= 49):
            sum_Points += 8 if(gender == 'M') else 10
            
    elif(50 <= age <= 59):
            sum_Points += 5 if(gender == 'M') else 7
        
    elif(60 <= age <= 69):
            sum_Points += 3 if(gender == 'M') else 4
        
    elif(70 <= age <= 79):
            sum_Points += 1 if(gender == 'M') else 2
 
    
#Check if the person is a smoker using an if statement and 
#Compute and add points to variable sum_Points based on the age using if-elif statements
#Using single line if-statments to save lines on code

if (is_Smoker == True):
        
        if(20 <= age <= 39):
            sum_Points += 8 if(gender == 'M') else 9

        elif(40 <= age <= 49):
            sum_Points += 5 if(gender == 'M') else 7
            
        elif(50 <= age <= 59):
            sum_Points += 3 if(gender == 'M') else 4
        
        elif(60 <= age <= 69):
            sum_Points += 1 if(gender == 'M') else 2
        
        elif(70 <= age <= 79):
            sum_Points += 1


#Check if the person is a non-smoker using an elif statement
#Compute and add points to variable sum_Points
  
elif (is_Smoker == False):
    sum_Points += 0


#Compute points based on HDL (mg/dL) using an if-elif statements
#Add the points to variable sum_Points
 
if (HDL_Cholestrol >= 60):
    sum_Points += -1
  
elif (50 <= HDL_Cholestrol <= 59):
    sum_Points += 0

elif (40 <= HDL_Cholestrol <= 49):
    sum_Points += 1

elif (HDL_Cholestrol < 40):
    sum_Points += 2

 
#Compute points based on systolic BP (mmHg) 
#Check if the patient is treated or untreated using nested-if, elif and else statement
#Using single line if-statments to save lines on code

if (systolic_BP < 120):
    sum_Points += 0
    
elif (120 <= systolic_BP <= 129):
    if(is_Treated == True):
        sum_Points += 1 if(gender == 'M') else 3

    else:
        sum_Points += 0 if(gender == 'M') else 1
     
elif (130 <= systolic_BP <= 139):
    if(is_Treated == True):
        sum_Points += 2 if(gender == 'M') else 4
    
    else:
        sum_Points += 1 if(gender == 'M') else 2

elif (140 <= systolic_BP <= 159):
    if(is_Treated == True):
        sum_Points += 2 if(gender == 'M') else 5
    
    else:
        sum_Points += 1 if(gender == 'M') else 3
        
elif (systolic_BP >= 160):
    if(is_Treated == True):
        sum_Points += 3 if(gender == 'M') else 6
    
    else:
        sum_Points += 2 if(gender == 'M') else 4

  
#Calculate the variable ten_year_risk_Percentage based on the variable sum_Points using if-elif statements

if ((gender == 'M' and sum_Points < 0) or (gender == 'F' and sum_Points < 9)):
    ten_year_risk_Percentage = '<1'

elif((gender == 'M' and 0 <= sum_Points <= 4) or (gender == 'F' and 9 <= sum_Points <= 12)) :
    ten_year_risk_Percentage = '1'

elif((gender == 'M' and 5 <= sum_Points <= 6) or (gender == 'F' and 13 <= sum_Points <= 14)):
    ten_year_risk_Percentage = '2'

elif((gender == 'M' and sum_Points == 7) or (gender == 'F' and sum_Points == 15)):
    ten_year_risk_Percentage = '3'
    
elif((gender == 'M' and sum_Points == 8) or (gender == 'F' and sum_Points == 16)):
    ten_year_risk_Percentage = '4'
    
elif((gender == 'M' and sum_Points == 9) or (gender == 'F' and sum_Points == 17)):
    ten_year_risk_Percentage = '5'

elif((gender == 'M' and sum_Points == 10) or (gender == 'F' and sum_Points == 18)):
    ten_year_risk_Percentage = '6'

elif((gender == 'M' and sum_Points == 11) or (gender == 'F' and sum_Points == 19)):
    ten_year_risk_Percentage = '8'        

elif(gender == 'M' and sum_Points == 12):
    ten_year_risk_Percentage = '10'

elif(gender == 'F' and sum_Points == 20):
    ten_year_risk_Percentage = '11'
  
elif(gender == 'M' and sum_Points == 13):
    ten_year_risk_Percentage = '12'

elif(gender == 'F' and sum_Points == 21):
    ten_year_risk_Percentage = '14'
    
elif(gender == 'M' and sum_Points == 14):
    ten_year_risk_Percentage = '16'

elif(gender == 'F' and sum_Points == 22):
    ten_year_risk_Percentage = '17'
    
elif(gender == 'M' and sum_Points == 15):
    ten_year_risk_Percentage = '20'
   
elif(gender == 'F' and sum_Points == 23):
    ten_year_risk_Percentage = '22'
    
elif(gender == 'M' and sum_Points == 16):
    ten_year_risk_Percentage = '25'
    
elif(gender == 'F' and sum_Points == 24):
    ten_year_risk_Percentage = '27'
    
elif((gender == 'M' and sum_Points >= 17) or (gender == 'F' and sum_Points >= 25)):
    ten_year_risk_Percentage = '>=30'

     
#Output the value of the variable ten_year_risk_Percentage to the Console using a print statement
print('\nYour 10-year risk of a heart attack is {:s}%.'.format(ten_year_risk_Percentage))    













    
    