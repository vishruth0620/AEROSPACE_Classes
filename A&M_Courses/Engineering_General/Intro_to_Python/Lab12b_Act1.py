#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 23:40:37 2020

@author: vishruth
"""

import turtle

def converttoroman(num):
    
    roman_Output = ''
    num,roman_Output = calculate_M(num,roman_Output)
    num,roman_Output = calculate_D(num,roman_Output)
    num,roman_Output = calculate_C(num,roman_Output)
    num,roman_Output = calculate_L(num,roman_Output)
    num,roman_Output = calculate_X(num,roman_Output)
    num,roman_Output = calculate_V(num,roman_Output)
    num,roman_Output = calculate_I(num,roman_Output)
    
    return roman_Output

def calculate_M(num,roman):
    if (num >= 1000):
        value = num // 1000
        for i in range(value):
            roman += 'M'
        
        num %= 1000
        
    return num,roman

def calculate_D(num,roman):
    if(400 <= num <= 499):
        roman += 'CD'
        num %= 400
    
    elif(900 <= num <= 999):
        roman += 'CM'
        num %= 900
        
    elif (num >= 500):
        value = num // 500
        for i in range(value):
            roman += 'D'
        
        num %= 500
        
    return num,roman

def calculate_C(num,roman):
    if(90 <= num <= 99):
        roman += 'XC'
        num %= 90
        
    elif (num >= 100):
        value = num // 100
        for i in range(value):
            roman += 'C'
        
        num %= 100
        
    return num,roman

def calculate_L(num,roman):
    if(90 <= num <= 99):
        roman += 'XC'
        num %= 90
    
    elif (num >= 50):
        value = num // 50
        for i in range(value):
            roman += 'L'
        
        num %= 50
        
    return num,roman

def calculate_X(num,roman):
    if(40 <= num <= 49):
        roman += 'XL'
        num %= 40
        
    elif (num >= 10):
        value = num // 10
        for i in range(value):
            roman += 'X'
        
        num %= 10
        
    return num,roman

def calculate_V(num,roman):
    if (num == 9):
        roman += 'IX'
        num %= 9
    
    elif (num >= 5):
        value = num // 5
        for i in range(value):
            roman += 'V'
        
        num %= 5
        
    return num,roman
        
def calculate_I(num,roman):
    if (num == 4):
        roman += 'IV'
        num %= 4
        
    elif (num >= 1):
        value = num // 1
        for i in range(value):
            roman += 'I'
        
        num %= 1
        
    return num,roman
        
        


number = int(input('Enter a number: '))

print('The roman numeral for {:d} is:'.format(number))
turtle.clear()
turtle.color('blue')
style = ('Times New Roman', 30, 'normal')
turtle.write(converttoroman(number), font=style, align='center')
turtle.hideturtle()