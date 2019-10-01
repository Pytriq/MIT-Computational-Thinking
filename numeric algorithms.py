# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 10:54:30 2019

@author: Patrick
"""

def findCbrt(x):
    """
    x : int or float, can also be negative
    returns the approximate cbrt of x
    uses bisection search algorithm
    """
    negFlag = False
    if x < 0:
        negFlag = True
        x = -x
    high = x
    numGuesses = 0
    epsilon = 0.001
    low = 1
    guess = (high + low)/2
        
    while abs(guess**3 - x) >= epsilon:
        if guess**3 > x:
            high = guess
        else:
            low = guess
        guess = (high + low)/2
        numGuesses += 1
    if negFlag:
        guess = -guess
    return guess

def findSqrt(x):
    """
    x : int or float, positive or negative
        less than or great than 1.
    returns the sqrt of x
    uses Newton-Raphton algorithm
    """
    negFlag = False
    if x < 0:
        negFlag = True
        x = -x
    epsilon = 0.001
    guess = x/2
    numGuesses = 0
    
    while abs(guess**2 - x) >= epsilon:
        numGuesses += 1
        guess = (guess - ((guess**2 - x)/(2*guess)))
    if negFlag:
        guess = -guess
    return guess

def numberGuesser():
    """
    uses bisection search algorithm to zero down to 
    a player's guess. 
    The game ends when player keys in c
    """
    print("Think of a number between 0 to 100, let me guess it")
    low = 0
    high = 100
    guess = (low + high)//2
    while True:
        print("Is your number", guess)
        entry = input("Enter l 4 low, h 4 high, c 4 correct: ")
        if entry == 'l':
            low = guess
        elif entry == 'h':
            high = guess
        elif entry == 'c':
            print("Game Over! Your Number is", guess)
            break
        else:
            print("Sorry, I didn't understand your entry!")
        
        guess = (high + low)//2
        
def apprxSqrt(x):
    """
    x can be any number less than or greater than 1
        int or float
    uses exhaustive algorithm
    returns apprx sqrt of x
    """
    negFlag = False
    if x < 0:
        negFlag = True
        x = -x
    epsilon = 0.001
    increment = 0.01 #keep epsilon less than increment
    guess = 0
    numGuesses = 0
    
    while abs(guess**2 - x) >= epsilon and guess**2 <= x:
        guess += increment
        numGuesses += 1
    if negFlag:
        print("Sorry, did you mean ", x)
    return guess

cbrt = findCbrt(23)
sqrt = apprxSqrt(625)
sqrt1 = findSqrt(625)
print(sqrt1)
print(sqrt)
print(cbrt)
#numberGuesser()

    
        
    
    
            
        
    
    
