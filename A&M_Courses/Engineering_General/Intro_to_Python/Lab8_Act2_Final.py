#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:09:56 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Michael Camacho, Liliana Salgado
# Course Header: Eng 102-451
# Assignment: Lab 7b Activity 1
# Date: 10/17/2020


list_Temperatures = [0,20,40,60,80,100,120,140,160,180,200,220,240,260]

#Properties at 5 Mega_Pascals
list_Volume = [0.0009977,0.0009996,0.0010057,0.0010149,0.0010267,0.0010410,0.0010576,0.0010769,0.0010988,0.0011240,0.0011531,0.0011868,0.0012268,0.0012755]
list_Internal_Energy = [0.04,83.61,166.92,250.29,333.82,417.65,501.91,586.8,672.55,759.47,847.92,938.39,1031.6,1128.5]
list_Enthalpy = [5.03,88.61,171.95,255.36,338.96,422.85,507.19,592.18,678.04,765.09,853.68,944.32,1037.7,1134.9]
list_Entropy = [0.0001,0.2954,0.5705,0.8287,1.0723,1.3034,1.5236,1.7344,1.9374,2.1338,2.3251,2.5127,2.6983,2.8841]

#Input a temperature from the user
input_Temperature = int(input('Enter a temperature between 0 and 260 C: '))


if(input_Temperature < 0 and input_Temperature > 260):
    print('The temperature doesn\'t satisfy within the ranges 0 to 260 C.')
    
else:
    for item in range(len(list_Temperatures)):
        
        if(list_Temperatures[item] <= input_Temperature <= list_Temperatures[item + 1]):
            
            slope_Volume = (list_Volume[item + 1] - list_Volume[item]) / (list_Temperatures[item + 1] - list_Temperatures[item])
            volume_Interpolation = (slope_Volume) * (input_Temperature - list_Temperatures[item]) + list_Volume[item]
            
            slope_Internal_Energy = (list_Internal_Energy[item + 1] - list_Internal_Energy[item]) / (list_Temperatures[item + 1] - list_Temperatures[item])
            internal_energy_Interpolation = (slope_Internal_Energy) * (input_Temperature - list_Temperatures[item]) + list_Internal_Energy[item]
            
            slope_Enthalpy = (list_Enthalpy[item + 1] - list_Enthalpy[item]) / (list_Temperatures[item + 1] - list_Temperatures[item])
            enthalpy_Interpolation = (slope_Enthalpy) * (input_Temperature - list_Temperatures[item]) + list_Enthalpy[item]
            
            slope_Entropy = (list_Entropy[item + 1] - list_Entropy[item]) / (list_Temperatures[item + 1] - list_Temperatures[item])
            entropy_Interpolation = (slope_Entropy) * (input_Temperature - list_Temperatures[item]) + list_Entropy[item]
            
            print('Properties at %.1f deg C are: ' % (input_Temperature))
            print('Specific volume (m^3/kg): %.7f' %  (volume_Interpolation))
            print('Specific internal energy (kJ/kg): %.2f' % (internal_energy_Interpolation))
            print('Specific enthalpy (kJ/kg): %.2f' % (enthalpy_Interpolation))
            print('Specific entropy (kJ/kgK): %.4f' % (entropy_Interpolation))
            break
            
            
         