#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:14:24 2020

@author: vishruth
"""
# Name: Vishruth Balaji
# Assignment Lab 2b Activity 2a
# Section: ENGR 102-451

error = str('\nThe given information is unable to be computed accurately.')

#Inputting values for the time intervals and positions for x
time1 = int(input('Enter time t1: ')) #seconds
time2 = int(input('Enter time t2: ')) #seconds
pos_check_time = int(input('Enter time to predict position: ')) #seconds

#Inputting values for the positions for x and 
#caluclating the position of x using linear interpolation
position_X1 = int(input('Enter position X1: ')) #meters
position_X2 = int(input('Enter position X2: ')) #meters
calc_pos_X0 = ((position_X2 - position_X1)/(time2 - time1)) * (pos_check_time - time1) + position_X1 

#Inputting values for the positions for y and 
#calculating the position of y using linear interpolation

position_Y1 = int(input('Enter position Y1: ')) #meters
position_Y2 = int(input('Enter position Y2: ')) #meters
calc_pos_Y0 = ((position_Y2 - position_Y1)/(time2 - time1)) * (pos_check_time - time1) + position_Y1 

#Inputting values for the positions for z and 
#caluclating the position of z using linear interpolation
position_Z1 = int(input('Enter position Z1: ')) #meters
position_Z2 = int(input('Enter position Z2: ')) #meters
calc_pos_Z0 = ((position_Z2 - position_Z1)/(time2 - time1)) * (pos_check_time - time1) + position_Z1

#limiting linear extrapolation because we are assuming a linear relationship between variables.
if pos_check_time >= time1 and pos_check_time <= time2 and pos_check_time != 0:
    #Output of position x0, y0 and z0 at a position check time
    print('At time', pos_check_time, 'seconds:\nx0 =', calc_pos_X0, 'm')
    print('y0 =', calc_pos_Y0, 'm')
    print('z0 =', calc_pos_Z0, 'm')
else:
    print(error)
    