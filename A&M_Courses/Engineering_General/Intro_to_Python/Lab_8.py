#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:03:42 2020

@author: vishruth
"""

# 	     By submitting this assignment I agree to the following
#          “Aggies do not, lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
#Name			Hunter Spier, Vishruth Balaji, Michael Camacho, Liliana Salgado
#Section		501
#Assignment		Lab8_Act2 Challenge
#Date			10/18/2020

#Properties for 5 MPA
v_5 = [0.0009977,0.0009996,0.0010057,0.0010149,0.0010267,0.0010410,0.0010576,0.0010769,0.0010988,0.0011240,0.0011531,0.0011868,0.0012268,0.0012755,0]#define list of values for v
u_5 = [0.04,83.61,166.92,250.29,333.82,417.65,501.91,586.8,672.55,759.47,847.92,938.39,1031.6,1128.5,0]#define list of values for u
h_5 = [5.03,88.61,171.95,255.36,338.96,422.85,507.19,592.18,678.04,765.09,853.68,944.32,1037.7,1134.9,0]#define list of values for h
s_5 = [0.0001,0.2954,0.5705,0.8287,1.0723,1.3034,1.5236,1.7344,1.9374,2.1338,2.3251,2.5127,2.6983,2.8841,0]#define lisrt of values for s

#Properties for 10MPA
v_10 = [0.0009952,0.0009973,0.0010035,0.0010127,0.0010244,0.0010385,0.0010549,0.0010738,0.0010954,0.0011200,0.0011482,0.0011809,0.0012192,0.0012653,0.0013226,0.0013980]
u_10 = [0.12,83.31,166.33,249.43,332.69,416.23,500.18,584.72,670.06,756.48,844.32,934.01,1026.2,1121.6,1221.8,1329.4]
h_10 = [10.07,93.28,176.37,259.55,342.94,426.62,510.73,595.45,681.01,767.68,855.8,945.82,1038.3,1134.3,1235,1343.3]
s_10 = [0.0003,0.2943,0.5685,0.826,1.0691,1.2996,1.5191,1.7293,1.9316,2.1271,2.3174,2.5037,2.6876,2.871,3.0565,3.2488]

def lin_int(a,n):#create function to linearly interpolate(a is the list to interpolate, n is the temperature input by the user)
    i = int(n//20)#find the index of the value to the left of the temperature value input
    m = n%20#find the diference between the index above and the temperature value input
    return ((m * (a[i+1] - a[i])) / 20) + a[i]#linearly interpolate amd output the value found

def lin_mpa(mpa,p5,p10):#create function to linearly interpolate(mpa is the pressure input by the user,p5 is interpolation at 5MPa, p10 is interpolation at 10MPa)
    m = (10 - mpa)/(10 - 5)#find the dslope for the pressure between 5 and 10MPa
    return (m * (p10-p5) + p5)#linearly interpolate amd output the value found


t = float(input('Enter a temperature between 0 and 260 C: '))#get the desired temperature from the user
p = float(input('Enter pressure between 5 and 10 MPa: '))#get the desired temperature from the user
if(0 <= t <= 260 and 5 <= p <= 10) :#determine whether the input temperature is within the valid range
    vi_5 = lin_int(v_5,t)#Find linear Interpolation for volume at 5MPA  by calling the lin_int() function
    vi_10 = lin_int(v_10,t)#Find linear Interpolation for volume at 10MPA by calling the lin_int() function
    ui_5 = lin_int(u_5,t)#Find linear Interpolation for internal energy at 5MPA  by calling the lin_int() function
    ui_10 = lin_int(u_10,t)#Find linear Interpolation for internal energy at 10MPA by calling the lin_int() function
    hi_5 = lin_int(h_5,t)#Find linear Interpolation for enthalpy at 5MPA  by calling the lin_int() function
    hi_10 = lin_int(h_10,t)#Find linear Interpolation for enthalpy at 10MPA by calling the lin_int() function
    si_5 = lin_int(s_5,t)#Find linear Interpolation for entropy at 5MPA  by calling the lin_int() function
    si_10 = lin_int(s_10,t)#Find linear Interpolation for entropy at 10MPA by calling the lin_int() function
    print('Properties at {} deg C and {} MPa are:\nSpecific volume (m^3/kg): {:.7f}\nSpecific internal energy (kJ/kg): {:.2f}\nSpecific enthalpy (kJ/kg): {:.2f}\nSpecific entropy (kJ/kgK): {:.4f}'.format(t,p,lin_mpa(p,vi_5,vi_10),lin_mpa(p,ui_5,ui_10),lin_mpa(p,hi_5,hi_10),lin_mpa(p,si_5,si_10)))#print the answer

else:
    print('Invalid temperature or pressure')#if the temperature value is not within the valid range print error
    
    
