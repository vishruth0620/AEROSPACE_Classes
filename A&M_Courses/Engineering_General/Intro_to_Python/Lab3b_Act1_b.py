#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:56:21 2020

@author: vishruth
"""
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 3b Activity 1b
# Date: 9/2/2020

import math

#This program is going to calculate /print the kinetic energy of the object in motion
print('\nThis program calculates the Kinetic Energy of the object.')
mass_Object = float(input('Please enter the mass of the object (kg): ')) #kilograms
velocity_Object = float(input('Please enter the velocity of the object (m/s): ')) #meterspersecond
kinetic_energy_Object = (mass_Object * math.pow(velocity_Object, 2)) / 2.0
print('\nThe Kinetic Energy of an object is %.1f', kinetic_energy_Object , 'J.')