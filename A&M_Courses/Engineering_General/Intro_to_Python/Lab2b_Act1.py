#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 08:05:24 2020

@author: vishruth
"""
# Name: Vishruth Balaji
# Assignment Lab 1B
# Section: ENGR 102-451

import math 

#This program is going to calculate/print the area of the rectangle with the length as 13 ft
#and the width as 16 ft

length_Rectangle = 13 #inches
width_Rectangle =  16 #inches

#To calculate the area of the rectangle, you will need to multiply 
#the length by the width

area_Rectangle = length_Rectangle * width_Rectangle #in^2
print()
print('The Area of the Rectangle is', area_Rectangle , 'inches^2.')

#This program is going to calculate/print the voltage across a conductor with a 
#resistance of 20 ohms and current of 5 amperes

resistance_Conductor = 20 #ohms
current_Conductor = 5 #amps

#To calculate the voltage across a conductor, you would simply multiply the resistance
#with the current

voltage_Conductor = resistance_Conductor * current_Conductor
print()
print('The Voltage across a conductor is', voltage_Conductor , 'V.')

#This program is going to calculate /print the kinetic energy of the object in motion with
#a mass of 100 kg and velocity of 21 m/s.

mass_Object = 100 #kg
velocity_Object = 21 #m/s

#To calculate the Kinetic Energy of an object, you would
#multiply the mass with the velocity and divide that answer by 2 

kinetic_energy_Object = (mass_Object * velocity_Object) / 2

print()
print('The Kinetic Energy of an object is', kinetic_energy_Object , 'J.')

#This program is going to calculate the Radioactive Decay of Radon-222 after 5 days given an
#initial amount of 3 grams and half-life of 3.8 days

initial_amount_Radon222 = 3 #grams
time_RadioActive_Decay = 5 #days
halflife_RadioActive_Decay = 3.8 #days

#To calculate the amount of Radon-222, you multiply the initial amount of Radon-222 by 2 to the power of negative time in days divided 
#by time of half-life
amount_left_Radon222 = float(initial_amount_Radon222 * (math.pow(2,-time_RadioActive_Decay/halflife_RadioActive_Decay)))

print()
print('The amount of Radon-222 left is', amount_left_Radon222 , 'g.')

#This program is going to calculate the shear stress on a material using the Mohr-Coulomb Criterion
#when the normal stress is 20lbf/in^2 is applied with a cohesion of 2lbf/in^2 at an angle of 35 degrees

normal_stress_Material = 20 #lbf/in^2
angle_Internal_Friction = 35 #degrees
cohesion_Material = 2 #lbf/in^2

shear_stress_Material = normal_stress_Material * math.tan(angle_Internal_Friction * (math.pi/180)) + cohesion_Material

print()
print('The Shear Stress of the material is' , shear_stress_Material , '\nlbf/in^2.')



