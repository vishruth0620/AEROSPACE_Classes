#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:23:19 2020

@author: vishruth
"""
# Name: Vishruth Balaji, Hunter Spier, Liliana Salgado, Michael Camacho
# Course Header: Eng 102-451
# Assignment: Lab 3b Activity 2
# Date: 9/3/2020

import math

#get the position components of the observer's position
observer_X = float(input('Enter the x position of the observer: '))
observer_Y = float(input('Enter the y position of the observer: '))
observer_Z = float(input('Enter the z position of the observer: '))

#get the position components of point 1
point1_X = float(input('Enter the x position of point 1: '))
point1_Y = float(input('Enter the y position of point 1: '))
point1_Z = float(input('Enter the z position of point 1: '))

#get the position components of point 2
point2_X = float(input('Enter the x position of point 2: '))
point2_Y = float(input('Enter the y position of point 2: '))
point2_Z = float(input('Enter the z position of point 2: '))

#output the positions of all three points to the screen in decimal
print('\nObserver Location is x = %3.2f y = %3.2f z = %3.2f' % (observer_X,observer_Y,observer_Z))
print('\n Point 1 Location is x = %3.2f y = %3.2f z = %3.2f' % (point1_X,point1_Y,point1_Z))
print('\n Point 2 Location is x = %3.2f y = %3.2f z = %3.2f' % (point2_X,point2_Y,point2_Z))

#compute the vector components of point 1 with respect to the observers position
x1 = point1_X - observer_X
y1 = point1_Y - observer_Y
z1 = point1_Z - observer_Z

#compute the vector components of point 2 with respect to the observers position
x2 = point2_X - observer_X
y2 = point2_Y - observer_Y
z2 = point2_Z - observer_Z

#calculate the angle formed by the two vectors, and convert from radians into degrees
angle_rads = math.acos(((x1 * x2) + (y1 * y2) + (z1 * z2))/(math.sqrt((x1 ** 2)+(y1 ** 2) + (z1 ** 2)) * math.sqrt((x2 ** 2) + (y2 ** 2) + (z2 ** 2))))
angle_deg = angle_rads * (180 / math.pi)
print('\nThe angle between the points is %.3f degrees.' % angle_deg)

