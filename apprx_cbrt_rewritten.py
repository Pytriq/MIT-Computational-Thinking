# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:08:52 2019

@author: Patrick
"""
#for good results, increment should be smaller than epsilon

cube = 29
increment = 0.001
epsilon = 0.01
num_guesses = 0
guess = 0.0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1

if abs(guess**3 - cube) >= epsilon:
    print("Failed to find the cuberoot")
else:
    print("Cuberoot of",cube,"is",guess)
print(num_guesses, "guesses")
