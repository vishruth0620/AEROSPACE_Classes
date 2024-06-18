#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:28:14 2020

@author: vishruth
"""
# Name: Vishruth Balaji
# Assignment Lab 1B: Activity 2
# Section: ENGR 102-451

from math import *

# This program is going to calculate the area of the rectangle with the length as 13 ft
# and the width as 16 ft.

# Display the values of the length and width of the rectangle
print("The length of the rectangle is 13 ft.")
print("The width of the rectangle is 16 ft.")

# To calculate the area of the rectangle, you will need to multiply 
# the length by the width
print("The Area of the Rectangle is", 13 * 16 ,"ft^2")


# This problem is going to calculate the voltage across a conductor
# using a resistance of 20 ohms and current of 5 amperes

# To calculate the voltage across a conductor, you would simply multiply the resistance
# with the current
print()
print("The Voltage across a Condutor is", 20 * 5 ,"volts.")


# This prgram is going to calculate the kinetic energy of the object in motion with
# a mass of 100 kg and velocity of 21 m/s.
# To calculate the Kinetic Energy of an object, you would
# multiply the mass with the velocity and divide that answer by 2 

print()
print("The Kinetic Energy of the object is", (100 * 21) / 2 , "joules");

# This program is going to calculate the Radioactive Decay of Radon-222 after 5 days given an
# initial amount of 3 grams and half-life of 3.8 days

print()
print("The radioactive decay of the Radon-222 after 5 days is", 3 * (2 ** (-5/3.8)) , "grams.")

# This program is going to calculate the shear stress on a material using the Mohr-Coulomb Criterion
#when the normal stress is 20lbf/in^2 is applied with a cohesion of 2lbf/in^2 at an angle of 35 degrees

print()
print("The shear stress of the material is" , 20 * tan(7 * pi / 36) + 2 , "lbf/in^2.")
