#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:58:27 2020

@author: vishruth
"""
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 3b Activity 1c
# Date: 9/2/2020

import math

#This program is going to calculate the Radioactive Decay of Radon-222 after 5 days given an
print('\nThis program is going to calculate the Radioactive Decay of Radon-222.')
initial_amount_Radon222 = float(input('Please enter the initial amount of grams of Radon-222 (grams): ')) #grams
time_RadioActive_Decay  = float(input('Please enter the time of Radioactive Decay (days): ')) #days
halflife_RadioActive_Decay = 3.8 #days
amount_left_Radon222 = float(initial_amount_Radon222 * (math.pow(2,-time_RadioActive_Decay/halflife_RadioActive_Decay)))
print('\nThe amount left of Radon-222 is %.3f' % (amount_left_Radon222), 'g.')