#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:04:07 2020

@author: vishruth
"""
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 3b Activity 1d
# Date: 9/2/2020

import math

#This program is going to calculate the shear stress on a material using the Mohr-Coulomb Criterion.
print('\nThis program is going to calculate the shear stress on a material using the Mohr-Coulomb Criterion.')
normal_stress_Material = float(input('Please enter the normal stress (lbf/in^2): ')) #lbf/in^2
angle_Internal_Friction =float(input('Please enter the angle of internal friction (degrees): ')) #degrees
cohesion_Material = float(input('Please enter the cohesion (lbf/in^2): ')) #lbf/in^2
shear_stress_Material = normal_stress_Material * (math.tan(angle_Internal_Friction * (math.pi/180))) + cohesion_Material
print('\nThe Shear Stress of the material is %.3f' % (shear_stress_Material), 'lbf/in^2.')