# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:34:14 2019

@author: Patrick
"""

#approximating cuberrot using try and check. guess
cube = 29
guess = 0.0
epsilon = 0.01
increment = 0.001
num_guesses = 0

while cube - guess**3 >= epsilon and guess**3 <= cube:
    guess += increment
    num_guesses += 1
if cube - guess**3 <= epsilon:
    print("The cuberoot of", cube,"is appr to",guess)
else:
    print("failed")
print("guesses : ", num_guesses)
    
    
