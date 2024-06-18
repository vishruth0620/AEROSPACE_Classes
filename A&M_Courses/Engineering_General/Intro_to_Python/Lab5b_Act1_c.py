#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:39:31 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 5b Activity 1c
# Date: 9/14/2020

num_Primes = 0 #Setting iteration counter to 0


for prime_Number in range(2, 101) : #Setting a for loop from 2 to 100
    number_Is_Prime = True #Setting if a number is prime to true
    
    for tester in range(2,prime_Number): #An inner for loop to test the variable prime number to values starting from 2
        if(prime_Number % tester == 0): # An if statement to chcek if the variable prime number has factors
            print(prime_Number, 'is not a prime number') #Printing variable prime number as not prime number
            number_Is_Prime = False #Setting number is prime to False
            break
    if (number_Is_Prime == True) :
         print(prime_Number, 'is a prime number') #Printing variable prime number  as a prime number
         num_Primes +=1 # Incrementing number of Primes by 1 as an iteration in the loop

print('\nThere are %d number of primes between 2 and 100.' % (num_Primes)) #Printting out the number of prime numbers between 2 and 100
