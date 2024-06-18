#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 20:34:38 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 11b Activity 1a
# Date: 11/5/2020


import math 

def parta(l,w,h,r):#Define a function of part A that passes parameters length, width, height and radius
    
    volume_Box = l * w * h#Creating a formula for volume of the box
    if (r < min(l/2,w/2)): #Check whether radius is less than minumum length and width
        volume_Cylinder = math.pi * math.pow(r,2) * h#Create a volume for the cylinder 
        volume_Difference = volume_Box - volume_Cylinder#Find the difference of Volume by subtracting the volume of cylinder from box 
        return volume_Difference #Return volume difference
    else:
        print('Try Again')
        


## Main Function ##
length = int(input('Enter a length: '))#Enter the length
width = int(input('Enter a width: '))#Enter the width
height = int(input('Enter a height: '))#Enter the height
radius = int(input('Enter a radius: '))#Enter the radius

print('The volume difference is {:.3f} units^3'.format(parta(length, width, height, radius)))#Calling the parta function and Printing the return values