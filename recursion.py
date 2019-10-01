# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:25:22 2019

@author: Patrick
"""

#finding the multplication of any two numbers
#Recursion is a programming technique where
#a function calls itself

def multiply(a, b):
    """
    a: int or float
    b: int
    returns the product of a and b
    """
    if b == 1: #base case
        return a
    else:
        return a + multiply(a, b-1) #recursive step
    
def factorial(n):
    """
    n: int
    returns the factorial of n
    """
    if n == 1:
        return 1 #base case
    else:
        return n*factorial(n-1) #recursive step
    
def power(b, e):
    """
    b: base, int or float
    e: int greater than or equal to 0
    returns b raised to power e
    """
    if e == 0:
        return 1 #base case
    else:
        return b * power(b, e-1) #recursive case
    
