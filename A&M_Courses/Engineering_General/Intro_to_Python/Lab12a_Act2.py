#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:15:41 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Michael Camacho, Hunter Spier, Liliana Salgado, Vishruth Balaji
# Section:      501
# Assignment:   Lab12a_Act2
# Date:         11/15/2020

import numpy as np

#making a list of functions, if they put 1 this will be the formula used 
def func1(x): 
    y1 = (x ** 3) + 1
    return y1

def func2(x): #If they put 2 for "num" input
    y2 = ((3 * x ** 3) + (2 * x ** 2) - (6 * x) + 5)
    return y2


def func3(x): #If they choose "3"
    y3 = ((2 * x ** 3) - (x ** 2) + (3 * x) - 2)
    return y3


#Input what polynomial to test, tpe a lower and upper bound integer number
print('Which polynomial would you like to test?\n1: x^3 + 1\n2: 3x^3 + 2x^2 - 6x + 5\n3: 2x^3 - x^2 + 3x - 2')
num = float(input('Enter the number: '))
print()
lvalue = float(input('Enter the lower value for the interval: '))
uvalue = float(input('Enter the upper value for the interval: '))
print()


# '''''''''num = "1"'''''''' #

# Shape 1 #
# left Riemann sum
if num == 1:
    counter = 10
    tol = 10e-6
    totalArea = 10
    while totalArea > tol:
        xvalues = np.linspace(lvalue, uvalue, counter + 1)

        w = xvalues[1] - xvalues[0]

        sum1 = 0
        for i in range(len(xvalues)):
            if i < max(range(len(xvalues))):
                sum1 += func1(xvalues[i]) * w

        counter += 10
        xvalues = np.linspace(lvalue, uvalue, counter + 1)
        w = xvalues[1] - xvalues[0]

        sum2 = 0
        for i in range(len(xvalues)):
            if i < max(range(len(xvalues))):
                sum2 += func1(xvalues[i]) * w

        totalArea = sum2 - sum1
        shape1 = sum2
    print('Shape 1 area:', round(sum2, 3))

## Shape 2 ##
# right Riemann sum
    counter = 10
    tol = 10e-6
    totalArea = 10
    while totalArea > tol:
        xvalues = np.linspace(lvalue, uvalue, counter + 1)

        w = xvalues[1] - xvalues[0]

        sum1 = 0
        for i in range(len(xvalues)):
            if i > min(range(len(xvalues))):
                sum1 += func1(xvalues[i]) * w

        counter += 10
        xvalues = np.linspace(lvalue, uvalue, counter + 1)
        w = xvalues[1] - xvalues[0]

        sum2 = 0
        for i in range(len(xvalues)):
            if i > min(range(len(xvalues))):
                sum2 += func1(xvalues[i]) * w

        totalArea = abs(sum2 - sum1)
        shape2 = sum2
    print('Shape 2 area:', round(sum2, 3))

### Shape 3 ####
# middle Riemann sum
    # midpoint = the avg of 1 and 2
    shape3 = (shape2 + shape1) / 2
    print('Shape 3 area: %.3f' % shape3)

#### Shape 4 #####

    counter = 10
    tol = 10e-6
    totalArea = 10
    while totalArea > tol:
        xvalues = np.linspace(lvalue, uvalue, counter + 1)

        w = xvalues[1] - xvalues[0]

        trap1 = 0
        for i in range(len(xvalues) - 1):
            trap1 += (func1(xvalues[i]) + func1(xvalues[i + 1])) * (1 / 2) * w

        counter += 500
        xvalues = np.linspace(lvalue, uvalue, counter + 1)
        w = xvalues[1] - xvalues[0]

        trap2 = 0
        for i in range(len(xvalues) - 1):
            trap2 += (func1(xvalues[i]) + func1(xvalues[i + 1])) * (1 / 2) * w

        totalArea = trap2 - trap1
    print('Shape 4 area: %.3f' % round(trap2, 3))


#''''''' num = 2 '''''''#

# Shape 1 #
# left Riemann sum
if num == 2:
    counter = 10
    tol = 10e-6
    totalArea = 10
    while totalArea > tol:
        xvalues = np.linspace(lvalue, uvalue, counter + 1)

        w = xvalues[1] - xvalues[0]

        sum1 = 0
        for i in range(len(xvalues)):
            if i < max(range(len(xvalues))):
                sum1 += func2(xvalues[i]) * w

        counter += 10
        xvalues = np.linspace(lvalue, uvalue, counter + 1)
        w = xvalues[1] - xvalues[0]

        sum2 = 0
        for i in range(len(xvalues)):
            if i < max(range(len(xvalues))):
                sum2 += func2(xvalues[i]) * w

        totalArea = abs(sum2 - sum1)
        shape1 = sum2
    print('Shape 1 area:', round(sum2, 3))


### Shape 2 ##
# right Riemann sum
    counter = 10
    tol = 10e-6
    totalArea = 10
    while totalArea > tol:
        xvalues = np.linspace(lvalue, uvalue, counter + 1)

        w = xvalues[1] - xvalues[0]

        sum1 = 0
        for i in range(len(xvalues)):
            if i > min(range(len(xvalues))):
                sum1 += func2(xvalues[i]) * w

        counter += 10
        xvalues = np.linspace(lvalue, uvalue, counter + 1)
        w = xvalues[1] - xvalues[0]

        sum2 = 0
        for i in range(len(xvalues)):
            if i > min(range(len(xvalues))):
                sum2 += func2(xvalues[i]) * w

        totalArea = abs(sum2 - sum1)
        shape2 = sum2
    print('Shape 2 area:', round(sum2, 3))

### Shape 3 ####
# middle Riemann sum
    # midpoint = the avg of 1 and 2
    shape3 = (shape2 + shape1) / 2
    print('Shape 3 area: %.3f' % shape3)


#### Shape 4 #####
    counter = 10
    tol = 10e-6
    totalArea = 10
    while totalArea > tol:
        xvalues = np.linspace(lvalue, uvalue, counter + 1)

        w = xvalues[1] - xvalues[0]

        trap1 = 0
        for i in range(len(xvalues) - 1):
            trap1 += (func2(xvalues[i]) + func2(xvalues[i + 1])) * (1 / 2) * w

        counter += 500
        xvalues = np.linspace(lvalue, uvalue, counter + 1)
        w = xvalues[1] - xvalues[0]

        trap2 = 0
        for i in range(len(xvalues) - 1):
            trap2 += (func2(xvalues[i]) + func2(xvalues[i + 1])) * (1 / 2) * w

        totalArea = trap2 - trap1
    print('Shape 4 area: %.3f' % round(trap2, 3))


#'''''''num = "3" ''''''''#

# Shape 1 #
# left
if num == 3:
    counter = 10
    tol = 10e-6
    totalArea = 10
    while totalArea > tol:
        xvalues = np.linspace(lvalue, uvalue, counter + 1)

        w = xvalues[1] - xvalues[0]

        sum1 = 0
        for i in range(len(xvalues)):
            if i < max(range(len(xvalues))):
                sum1 += func3(xvalues[i]) * w

        counter += 10
        xvalues = np.linspace(lvalue, uvalue, counter + 1)
        w = xvalues[1] - xvalues[0]

        sum2 = 0
        for i in range(len(xvalues)):
            if i < max(range(len(xvalues))):
                sum2 += func3(xvalues[i]) * w

        totalArea = abs(sum2 - sum1)
        shape1 = sum2
    print('Shape 1 area:', round(sum2, 3))

## Shape 2 ##
# right Riemann sum
    counter = 10
    tol = 10e-6
    totalArea = 10
    while totalArea > tol:
        xvalues = np.linspace(lvalue, uvalue, counter + 1)

        w = xvalues[1] - xvalues[0]

        sum1 = 0
        for i in range(len(xvalues)):
            if i > min(range(len(xvalues))):
                sum1 += func3(xvalues[i]) * w

        counter += 10
        xvalues = np.linspace(lvalue, uvalue, counter + 1)
        w = xvalues[1] - xvalues[0]

        sum2 = 0
        for i in range(len(xvalues)):
            if i > min(range(len(xvalues))):
                sum2 += func3(xvalues[i]) * w

        totalArea = abs(sum2 - sum1)
        shape2 = sum2
    print('Shape 2 area:', round(sum2, 3))

### Shape 3 ###
# middle Riemann sum
    # midpoint = the avg of 1 and 2
    shape3 = (shape2 + shape1) / 2
    print('Shape 3 area: %.3f' % shape3)

#### Shape 4 ####
    counter = 10
    tol = 10e-6
    totalArea = 10
    while totalArea > tol:
        xvalues = np.linspace(lvalue, uvalue, counter + 1)

        w = xvalues[1] - xvalues[0]

        trap1 = 0
        for i in range(len(xvalues) - 1):
            trap1 += (func3(xvalues[i]) + func3(xvalues[i + 1])) * (1 / 2) * w

        counter += 500
        xvalues = np.linspace(lvalue, uvalue, counter + 1)
        w = xvalues[1] - xvalues[0]

        trap2 = 0
        for i in range(len(xvalues) - 1):
            trap2 += (func3(xvalues[i]) + func3(xvalues[i + 1])) * (1 / 2) * w

        totalArea = trap2 - trap1
    print('Shape 4 area: %.3f' % round(trap2, 3))