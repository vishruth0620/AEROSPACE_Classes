#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:43:50 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Michael Camacho, Liliana Salgado
# Course Header: Eng 102-451
# Assignment: Lab 7b Activity 1
# Date: 9/29/2020

#Input the name of person
name_Person = input('What is your name? ')

#Set the variable check_Consonant to the first element in the string
check_Vowel = name_Person[0]

#Check if the check Consonant is a vowel or a consonant
#Change the first letter of the name_Person to lowercase if it's a vowel, else print the name_Person without the first letter
if((check_Vowel == 'A') or (check_Vowel == 'E') or (check_Vowel == 'I') or (check_Vowel == 'O') or (check_Vowel == 'U')):
    name_Person1 = name_Person.replace(check_Vowel,check_Vowel.lower())
    update_Phrase1 = ('Bo-B%s' % (name_Person1))   
    update_Phrase2 = ('Fo-F%s' % (name_Person1))                                                                                                      
    update_Phrase3 = ('Mo-M%s' % (name_Person1)) 
    
else:
    name_Person1 = name_Person[1:]
    update_Phrase1 = ('Bo-B%s' % (name_Person1))   
    update_Phrase2 = ('Fo-F%s' % (name_Person1))                                                                                                      
    update_Phrase3 = ('Mo-M%s' % (name_Person1)) 
    

#Otuput the story line with the updated phrases to the console
print('%s, %s, %s, \nBanana-Fana %s \nMe Mi %s \n%s! ' % (name_Person,name_Person,update_Phrase1,update_Phrase2,update_Phrase3,name_Person))  
    