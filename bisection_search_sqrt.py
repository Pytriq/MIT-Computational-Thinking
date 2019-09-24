# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:52:52 2019

@author: Patrick
"""

x = 9
epsilon = 0.001
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2

while abs(ans**2 - x) >= epsilon:
    if ans**2 > x:
        high = ans
    else:
        low = ans
    ans = (high + low)/2
    numGuesses += 1
print(ans, "is close to the squareroot of", x)
print("Guesses", numGuesses)
