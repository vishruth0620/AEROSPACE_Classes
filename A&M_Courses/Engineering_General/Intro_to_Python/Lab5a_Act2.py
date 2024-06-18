#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 19:51:37 2020

@author: vishruth
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 5a Activity 1
# Date: 9/14/2020

#################### Part A ####################
from sympy import *
x = symbols('x')
h = symbols('h')
coefDi = 2#int(input('Please enter the coefficient A: '))
coefAi = 3#int(input('Please enter the coefficient B: '))  #user imput coeficient A
coefBi = -11#int(input('Please enter the coefficient C: '))  #user imput coeficient B
coefCi = -6#int(input('Please enter the coefficient D: '))  #user imput coeficient C
coefD = coefDi
coefA = coefAi     #crreating alternate coeficients to alter while keeping initial values
coefB = coefBi
coefC = coefCi
coefD_sign = ' '
coefA_sign = ' + '    #initial signs to fill spots for equation
coefB_sign = ' + '
coefC_sign = ' + ' 
if coefD < 0:
    coefD_sign = ' - '
    coefD = abs(coefD)
if coefD == 0:
    coefD = ''
    coefA_sign = ''
elif coefD == 1:
    coefD = '(x)**3'
else:
    coefD = str(coefD) + '*(x)**3'
termD = '{}{}'.format(coefD_sign, coefD)
if coefA < 0:    #creating x^2 term
    coefA_sign = ' - '
    coefA = abs(coefA)
if coefA == 0:
    coefA = ''
    coefA_sign = ''
elif coefA == 1:
    coefA = '(x)**2'
else:
    coefA = str(coefA) + '*(x)**2'
termA = '{}{}'.format(coefA_sign, coefA)
if coefB < 0:    #creating x term
    coefB_sign = ' - '
    coefB = abs(coefB)
if coefB == 0:
    coefB = ''
    coefB_sign = ''
elif coefB == 1:
    coefB = '(x)'
else:
    coefB = str(coefB) + '*(x)'
termB = '{}{}'.format(coefB_sign, coefB)
if coefC < 0:    #creating constant term
    coefC_sign = ' - '
    coefC = abs(coefC)
if (coefA == '' and coefB == '') and (coefC == 0 and coefD == 0) :
    coefC = 0
    coefC_sign = ''
elif coefC == 0:
    coefC = ''
    coefC_sign = ''
else:
    coefC = str(coefC)
termC = '{}{}'.format(coefC_sign, coefC)
equation = '{}{}{}{}'.format(termD, termA, termB, termC) #combining terms to form equation
#################### Part B ####################
valx = '-2'#(input('Enter a value for x: '))
fx = float(simplify(equation.replace('x',valx)))
print(fx)
#################### Part C ####################
equation1 = equation.replace('x','x + h')
equation2 = equation.replace('x','x - h')
der_equation1 = '({} - ({}))'.format(equation1,equation)
der_equation2 = '({} - ({}))'.format(equation,equation2)
der_equation3 = '({} - ({}))'.format(equation1,equation2)
derivative1 = str(der_equation1)
derivative1 = derivative1.replace('x',valx)
derivative1 = '{}/h'.format(derivative1)
derivative_analytical = str(derivative1.replace('h', '0'))
derivative2 = str(der_equation2)
derivative2 = derivative2.replace('x',valx)
derivative2 = '{}/h'.format(derivative2)
derivative3 = str(der_equation3)
derivative3 = derivative3.replace('x', valx)
derivative3 = '{}/(2*h)'.format(derivative3)



difference = 1
n = 0
while (difference >= 0.000001) or (difference <= -0.000001):
    n += 1
    answer1 = str(simplify(derivative1.replace('h','((0.1)/2**{})'.format(n))))
    last_answer = str((derivative1.replace('h','((0.1)/2**{})'.format(n - 1))))
    difference = simplify('{} - {}'.format(answer1,last_answer))
difference = 1
n = 0
print(answer1)
while (difference >= 0.000001) or (difference <= -0.000001):
    n += 1
    answer1 = str(simplify(derivative2.replace('h','((0.1)/2**{})'.format(n))))
    last_answer = str((derivative2.replace('h','((0.1)/2**{})'.format(n - 1))))
    difference = simplify('{} - {}'.format(answer1,last_answer))
difference = 1
n = 0
print(answer1)
while (difference >= 0.000001) or (difference <= -0.000001):
    n += 1
    answer1 = str(simplify(derivative3.replace('h','((0.1)/2**{})'.format(n))))
    last_answer = str((derivative3.replace('h','((0.1)/2**{})'.format(n - 1))))
    difference = simplify('{} - {}'.format(answer1,last_answer))
print(answer1)



