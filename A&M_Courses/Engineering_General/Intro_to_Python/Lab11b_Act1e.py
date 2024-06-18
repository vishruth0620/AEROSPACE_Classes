#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:41:22 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 11b Activity 1e
# Date: 11/5/2020


def parte(list_Nums):#Define method parte with a parameter of list of Numbers
    
    min_Num = 999 #Create a variable min_Num and assign it to 999
    max_Num = 0 #Create a variable max_Num and assign it to 0
    sum_Nums = 0 #Create a sum_Nums variable and set it to 0
    
    for i in range(len(list_Nums)):#Use a for loop to go through each value of the list_Nums
        
        if(list_Nums[i] < min_Num):#Chencking for minimum number
            min_Num = list_Nums[i]#Setting min_Num to the minimum number in the list
        
        if(list_Nums[i] > max_Num):#Chencking for maximum number
            max_Num = list_Nums[i]#Setting max_Num to the maximum number in the list
        
        sum_Nums += list_Nums[i]#Computating the sums for the numbers in the list
    
    mean_Nums = sum_Nums / len(list_Nums) #Finding the mean of the list
    return 'Maximum: {:d}\nMean: {:.2f}\nMaximum: {:d}'.format(min_Num,mean_Nums,max_Num) #Returning the min_Num, max_num and mean_Nums 


## Main Function ##

list_Numbers = [539,479,135,286,782]#Numbers of Test Case 1
print(parte(list_Numbers))#Call and Print method from Test Case 1

list_Numbers2 = [65,178,1987,986,345]#Numbers of Test Case 2
print('\n'+ parte(list_Numbers2))#Call and Print method from Test Case 2

list_Numbers3 = [373,109,3475,675,3097]#Numbers of Test Case 3
print('\n'+ parte(list_Numbers3))#Call and Print method from Test Case 3