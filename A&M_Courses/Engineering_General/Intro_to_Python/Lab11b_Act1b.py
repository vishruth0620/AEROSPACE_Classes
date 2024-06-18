#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:02:35 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 11b Activity 1b
# Date: 11/5/2020


def partb(facilities,annual_cost,product_Value): #Define a function that takes parameters of facilities,
    least_Profit = 99999
    fi = 0
    for i in range(len(facilities)):
        net_Profit = product_Value[i] - annual_cost[i]
        if (net_Profit < least_Profit):
            least_Profit = net_Profit
            fi = i
    
    return facilities[fi],least_Profit


## Main Function ##
facilities_1 = ['FRABA sp z.o.o.','Nestle Factory','Shell Factory','Intel’s Fab32','Volkswagen’s Transparent Factory']#Create a Test Case 1
annual_cost_1 = [1200,1004,1600,1230,9760]#Create annual costs for Test Case 1
product_Value_1 = [4000,3000,4000,5000,12000]#Create value of products for Test Case 1
print('Least Profitable:',partb(facilities_1,annual_cost_1,product_Value_1))#Call and Print method from Test Case 1

facilities_2 = ['FRABA sp z.o.o.','Nestle Factory','Shell Factory','Intel’s Fab32','Volkswagen’s Transparent Factory']#Create a Test Case 2
annual_cost_2 = [136,508,698,806,974]#Create annual costs for Test Case 2
product_Value_2 = [4000,3000,4500,5000,3000]#Create value of products for Test Case 2
print('Least Profitable:',partb(facilities_2,annual_cost_2,product_Value_2))#Call and Print method from Test Case 2

facilities_3 = ['FRABA sp z.o.o.','Nestle Factory','Shell Factory','Intel’s Fab32','Volkswagen’s Transparent Factory']#Create a Test Case 3
annual_cost_3 = [139,528,793,506,978]#Create annual costs for Test Case 3
product_Value_3 = [4000,3000,4500,1000,7000]#Create value of products for Test Case 3
print('Least Profitable:',partb(facilities_3,annual_cost_3,product_Value_3))#Call and Print method from Test Case 3