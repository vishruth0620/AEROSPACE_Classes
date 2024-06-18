#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:12:57 2020

@author: vishruth
"""
# Name: Vishruth Balaji
# Assignment Lab 1B
# Section: ENGR 102-451


print("Howdy, World!")
print("I'm a 6-footer and love to play basketball.")
print()

import math
# This program is going to calculate the area of the rectangle with the length as 13 ft
# and the width as 16 ft

# Display the values of the length and width of the rectangle
print("The length of the rectangle is 13 ft.")
print("The width of the rectangle is 16 ft.")

# To calculate the area of the rectangle, you will need to multiply 
# the length by the width
print("The Area of the Rectangle is", 13 * 16 ,"ft^2.")


# This problem is going to calculate the voltage across a conductor
# using a resistance of 20 ohms and current of 5 amperes

# To calculate the voltage across a conductor, you would simply multiply the resistance
# with the current
print()
print("The Voltage across a Condutor is", 20 * 5 ,"volts.")


# This program is going to calculate the kinetic energy of the object in motion with
# a mass of 100 kg and velocity of 21 m/s.
# To calculate the Kinetic Energy of an object, you would
# multiply the mass with the velocity and divide that answer by 2 

print()
print("The Kinetic Energy of the object is", (100 * 21)**2 / 2 , "joules.");

# This program is going to calculate the Radioactive Decay of Radon-222 after 5 days given an
# initial amount of 3 grams and half-life of 3.8 days

print()
print("The radioactive decay of the Radon-222 after 5 days is", 3 * (2 ** (-5/3.8)) , "grams.")

# This program is going to calculate the shear stress on a material using the Mohr-Coulomb Criterion
# when the normal stress is 20lbf/in^2 is applied with a cohesion of 2lbf/in^2 at an angle of 35 degrees

print()
print("The shear stress of the material is" , 20 * math.tan(7 * math.pi / 36) + 2 , "lbf/in^2.")

print()
print("This program states the tasks for the evaluating function ln(x)/x that approaches x=0.")
print()
print("My guess for the final calculated value for 0.000001 is -200000000.")
print()
print(math.log(1)/1)
print(math.log(0.1)/0.1)
print(math.log(0.01)/0.01)
print(math.log(0.001)/0.001)
print(math.log(0.0001)/0.0001)
print(math.log(0.00001)/0.00001)
print(math.log(0.000001)/0.000001)
print(math.log(0.0000001)/0.0000001)
print()
print("My guess was slighty close to the final calculated value.")