#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:04:54 2020

@author: vishruth
"""
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 3b Activity 1a
# Date: 9/2/2020



#This program is going to calculate/print the voltage across a conductor
print('\nThis program calculates the voltage across a conductor.')
resistance_Conductor = float(input('Please enter the resistance (ohms): ')) #ohms
current_Conductor = float(input('Please enter the current (amps): ')) #amps
voltage_Conductor = resistance_Conductor * current_Conductor #Volts
print('\nThe Voltage across a conductor is %.1f' % (voltage_Conductor), 'V.')


