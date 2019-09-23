# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:02:21 2019

@author: Patrick
"""
#tricky infinite loop.
#when the substitution of if is really small 
#if evealuates to false and guess does not change anymore
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step
#    else:
#        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
