# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:36:59 2019

@author: Patrick
"""

# for approximating root of a polynomial in 1 variable
#guess = guess - (((guess**2) - k)/(2*guess))

epsilon = 0.01
k = 625
guess = k/2.0
numGuess = 0
while abs(guess**2 - k) >= epsilon:
    numGuess +=1
    guess = guess - (((guess**2) - k)/(2*guess))

print("Guesses", numGuess)
print("Apprx root of", k, "is", guess)
