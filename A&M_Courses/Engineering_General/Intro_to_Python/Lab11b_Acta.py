#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 23:50:38 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 11a Activity 1
# Date: 11/5/2020

import math 


def parta(l,w,h,r):
    
    volume_Box = l * w * h
    if (r < min(l/2,w/2)): 
        volume_Cylinder = math.pi * math.pow(r,2) * h
        volume_Difference = volume_Box - volume_Cylinder
        return volume_Difference
    else:
        return 0.0

def partb(facilities,annual_cost,product_Value):
    least_Profit = 99999
    fi = 0
    for i in range(len(facilities)):
        net_Profit = product_Value[i] - annual_cost[i]
        if (net_Profit < least_Profit):
            least_Profit = net_Profit
            fi = i
    
    return facilities[fi],least_Profit

def partc(na,ad,ci,sta,zip_c):
    
    return '{:s}\n{:s}\n{:s}, {:s} {:d}'.format(na,ad,ci,sta,zip_c)

def partd(file_Name):
    out_FileName = file_Name.replace('csv','tsv')
    file_1 = open(file_Name,'r') 
    file_2 = open(out_FileName,'w')
    for line in file_1:
        list_Values = line.split(',')
        for value in list_Values:
             file_2.write(value + '\t')
        
        file_2.write('\n')
    
    file_1.close()
    file_2.close()

def parte(list_Nums):
    
    min_Num = 999
    max_Num = 0
    sum = 0
    for i in range(len(list_Nums)):
        
        if(list_Nums[i] < min_Num):
            min_Num = list_Nums[i]
        
        if(list_Nums[i] > max_Num):
            max_Num = list_Nums[i]
        
        sum += list_Nums[i]
    
    mean = sum / len(list_Nums)
    return '{:d}\n{:f}\n{:d}'.format(min_Num,mean,max_Num)

            
def partf(list_Time,list_Distance):
    list_Average_Velocity = []
    average_Velocity = 0.0
    for i in range(len(list_Time) - 1):           
        average_Velocity = (list_Distance[i+1] - list_Distance[i]) / (list_Time[i+1] - list_Time[i])
        list_Average_Velocity.append(average_Velocity)
    
    return list_Average_Velocity
    



#print(parta(5, 6, 7, 2))

#list_1 = ['fi','bi','ci','di','ei']
#list_2 = [1200,1004,1600,1230,9760]
#list_3 = [4000,3000,4000,5000,12000]
#print(partb(list_1,list_2,list_3))

#print(partc('Critter, Ess S','123 Faux St.','Alexandria','VA',23310))

#partd('NBA.csv')

#list_Numbers = [539,479,135,286,782]
#print(list_Numbers)
#print(parte(list_Numbers))

list_Times = [1,2,3,4,5,6,7,8]
print(len())
list_Distances = [25,36,48,74,82,56,90,117]
print(partf(list_Times,list_Distances))
