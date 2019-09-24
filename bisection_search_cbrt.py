# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:08:53 2019

@author: Patrick
"""
cube = 27
epsilon = 0.001
high = cube
low = 1.0
guess = (high + low)/2
numGuess = 0
while abs(guess**3 - 27) >= epsilon:
    if guess**3 > cube:
        high = guess
    else:
        low = guess
    guess = (low + high)/2
    numGuess += 1
    
print(guess, "is the apprx cbrt of",cube)
print("Guesses",numGuess)

