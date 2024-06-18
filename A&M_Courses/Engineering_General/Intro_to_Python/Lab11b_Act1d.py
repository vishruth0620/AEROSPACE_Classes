#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:34:16 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 11b Activity 1d
# Date: 11/5/2020

def partd(file_Name): #Define a function partd that takes a parameter file name
    out_FileName = file_Name.replace('csv','tsv')#Relpace the extension of the file to tsv
    file_1 = open(file_Name,'r') #Open the CSV File for reading
    file_2 = open(out_FileName,'w')#Open the TSV file for writing
    for line in file_1:#Read each line in the csv file
        list_Values = line.split(',')#Create a list of each value as a string in the line with a split method of comma
        for value in list_Values:#Taking each value in the list
             file_2.write(value + '\t')#Writing it to file 2 with tabs using an escape character (TSV is Tab-Seperating Values)
        
        file_2.write('\n')#Create a new line for the next line
    
    file_1.close()#Close file 1
    file_2.close()#Close file 2
    


## Main Function ##
file_User = input('Enter a file name and save it as a CSV file (.csv extension): ')#Input a file name with .csv extension
partd(file_User)#Call method partd