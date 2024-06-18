#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:41:43 2020

@author: vishruth
"""
# Name: Vishruth Balaji
# Assignment Lab 2b Activity 2c
# Section: ENGR 102-451

error = str('\nThe given information is unable to be computed accurately.')

#Inputting values for the time intervals and positions for x, y and z
time1 = int(input('Enter time t1: ')) #seconds
time2 = int(input('Enter time t2: ')) #seconds
starting_interpolation_Time = int(input('Enter starting time for interpolation: ')) #seconds
ending_interpolation_Time = int(input('Enter ending time for interpolation: ')) #seconds
spacing_interpolation_Time = float(input('Enter spacing for the interpolation: ')) #times
position_X1 = int(input('Enter position X1: ')) #meters
position_X2 = int(input('Enter position X2: ')) #meters
position_Y1 = int(input('Enter position Y1: ')) #meters
position_Y2 = int(input('Enter position Y2: ')) #meters
position_Z1 = int(input('Enter position Z1: ')) #meters
position_Z2 = int(input('Enter position Z2: ')) #meters
print('\n')

#limiting linear extrapolation because we are assuming a linear relationship between variables.
if starting_interpolation_Time >= time1 and ending_interpolation_Time <= time2:
    
    pos_check_time = starting_interpolation_Time
    while pos_check_time <= ending_interpolation_Time:

        #Caluclating the position of x using linear interpolation
        calc_pos_X0 = ((position_X2 - position_X1)/(time2 - time1)) * (pos_check_time - time1) + position_X1 

        #Calculating the position of y using linear interpolation
        calc_pos_Y0 = ((position_Y2 - position_Y1)/(time2 - time1)) * (pos_check_time - time1) + position_Y1 

        #Caluclating the position of z using linear interpolation
        calc_pos_Z0 = ((position_Z2 - position_Z1)/(time2 - time1)) * (pos_check_time - time1) + position_Z1

        #Output of position x0, y0 and z0 at a position check time
        print('At time', pos_check_time, 'seconds:\nx0 =', calc_pos_X0, 'm')
        print('y0 =', calc_pos_Y0, 'm')
        print('z0 =', calc_pos_Z0, 'm')
        print('------------------')
        
        pos_check_time += spacing_interpolation_Time
else:
     print(error)
