# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:35:47 2019

@author: Patrick
"""
print("Please think of a number btn 0 and 100!")
low = 0
high = 100
guess = (low + high)//2
while True:
    print("Is your number", guess)
    entry = input("Enter h 4 high, l 4 low, c 4 correct")
    if entry == 'l':
        low = guess
    elif entry == 'h':
        high = guess
    elif entry == 'c':
        print("Game over. Your secret number was:", guess)
        break
    else:
        print("Sorry, I did not understand your input.")
    guess = (high + low)//2


