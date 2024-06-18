#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 00:43:09 2020

@author: vishruth
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 11b Activity 2
# Date: 11/5/2020

import random as rm

def assign_number():#Create a function to generate a random number to guess from 1 to 100
    
    return rm.randint(1,101)#Generated random number between 1 and 100

def guess_too_low(num,guess):#Define a function too low taking parameters num and guess
    
    if(guess < num):#If your guess is less than secret number 
        print('Too Low!') #Print Too Low
        
def guess_too_high(num,guess):#Define a function too high taking parameters num and guess
    
    if(guess > num):#If your guess is higher than secret number 
        print('Too High!')#Print Too High
    
    
secret_Number = assign_number()#Call assign number to assign to secret number
print('Guess the secret number! Hint: it’s an integer between 1 and 100...') #Input your first guess
guess_Number = 0#Set the guess number equal to ero as an input variable
num_Guesses = 0#Set a counter variable taking number of Guesses to 0
while (guess_Number != secret_Number): #Looping when guess number is not equal to secret number
    guess_Number =  int(input('What is your guess? '))#Inputing the number
    guess_too_low(secret_Number, guess_Number)#Calling function guess low
    guess_too_high(secret_Number, guess_Number)#Calling function guess high
    num_Guesses += 1 #Incrementing number of Guesses by 1

print('\nYou guessed it! It took you {:d} guesses.'.format(num_Guesses))#printing the number of guesses to reach the secret number
