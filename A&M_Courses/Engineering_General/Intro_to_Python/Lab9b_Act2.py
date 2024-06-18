#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:28:33 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji
# Course Header: Eng 102-451
# Assignment: Lab 9b Activity 2
# Date: 10/20/2020

import math
#Method to Calculate the monthly payment using loans months and rate as parameters
def calculate_monthly_payment(loan,months,rate):
    
    monthly_rate = rate / 12 #Calculate interest rate per month
    monthly_Payment = (loan * monthly_rate) / (1 - math.pow(1 / (1 + monthly_rate),months)) # Formula to find monthly payment
    return monthly_Payment #Return the Monthly Payment


user_file = input('Enter output file: ') #Input a file name
amount_Loan = int(input('Enter the principal amount: ')) #Input a principal amount
term_Length_Months = int(input('Enter term length (months): ')) #Input a term length in months
annual_Interest_Rate = float(input('Enter annual interest rate: '))#Input a interest rate per year
file = open(user_file,'w')#Open the input file for writing
file.write('Month,Total Accrued Interest,Loan\n')#Print the header
file.write('0,$0.00,%.2f\n' % (amount_Loan))#Print he second line with starting loan
accrued_Interest = 0.00 #Initializing variable for accrued interest
remaining_Balance = amount_Loan #Set a calculate variable
monthly_Payment = calculate_monthly_payment(amount_Loan,term_Length_Months,annual_Interest_Rate)#Use the monthly payment from method to use for the while loop
count_Months = 1#Initialize a counter for months to 1

while(remaining_Balance >= 0.01):#Set a while loop to loop until the remaining balance is less than $0.01
    monthly_Interest = (remaining_Balance * (annual_Interest_Rate / 12)) #Calculate the Monthly Interest
    accrued_Interest += monthly_Interest#Add the Monthly Interest to the Accrued Interest
    remaining_Balance = (monthly_Interest + remaining_Balance) - monthly_Payment#Find the remaining balance depending on change in monthly_interest in while loop
    file.write('%d,$%.2f,$%.2f\n' % (count_Months,accrued_Interest,remaining_Balance))#Output to the writing file the months, the accrued interest and remaining balance
    count_Months += 1#Increment the number of months by 1
    
#Close file to prevent malfunction
file.close()