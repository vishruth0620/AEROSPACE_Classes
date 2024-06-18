#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 08:08:04 2020

@author: vishruth
"""
# Name: Vishruth Balaji
# Assignment Lab 2A Activity 3
# Section: ENGR 102-451

import math


error = str('\nThe given information is unable to be computed accurately.')
user_choice = int(input('Would you like to see our output for Part 1 or Part 2?\nEnter 1 to see Part 1\nEnter 2 to see Part 2\nEnter Answer: '))

#Part 1
#starting by entering variables
if user_choice == 1:

    time_initial = int(input('Initial time measurement: '))
    time_final = int(input('Final time measurement: '))
    pos_initial = int(input('Initial location: '))
    pos_final = int(input('Final location: '))
    pos_check_time = int(input('Time to predict location: '))
    calc_pos = ((pos_check_time - time_initial) * (pos_final - pos_initial) / (time_final - time_initial)) + pos_initial
    #checking to ensure if the selected time on position is not to linearly extrapolate
    if pos_check_time >= time_initial and pos_check_time <= time_final and pos_check_time != 0:
    #output
        print('position at time =', pos_check_time, 'is', calc_pos, 'meters.' '\nThis means that given the current speed, and assuming constant velocity, at the time input the car will have traveled this far.')
    else:
        # 
            print(error)
elif user_choice == 2:
    #Part 2
    lap_distance = math.pi * (int(input('Enter track radius: ')) * 2) #meters 
    time_initial = int(input('Initial time measurement: '))
    time_final = int(input('Final time measurement: '))
    pos_initial = int(input('Initial location: '))
    pos_final = int(input('Final location: '))
    pos_check_time = int(input('Time to predict location: '))
    calc_pos = ((pos_check_time - time_initial) * (pos_final - pos_initial) / (time_final - time_initial)) + pos_initial

    distance_from_start = calc_pos % lap_distance
    #not limiting linear extrapolation because we are asuming a linear relationship between variables.
    #output
    print('Position in lap is', distance_from_start, 'at time', pos_check_time, '\nThis means that given the current speed, and assuming constant velocity, at the time imput the car will be this far from the starting line.')
else:
    print('No valid answer.')