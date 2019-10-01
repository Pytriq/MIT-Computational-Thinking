# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:46:38 2019

@author: Patrick
"""

def printName(firstName, lastName, reverse):
    """
    firstName and lastName : String
    if reverse is False, the names are reversed
    """
    if reverse:
        print(lastName, firstName)
    else:
        print(firstName, lastName)

def justName(fName = "John", lName = "Doe", reverse = False):
    """
    if no argument is passed, default name John Doe
    is printed.
    """
    if reverse:
        print(lName, fName)
    else:
        print(fName, lName)

def lastNamer(fName, lName = 'Riungu', reverse=False):
    """
    you can pass all arguments or just firstname
    """
    if reverse:
        print(lName, fName)
    else:
        print(fName, lName)
    
def foo(x, y = 4):
    """
    x, y: int or float
    returns evaluation of private function
    Note: private function variables are private to it!!!
    """
    def bar(x):#private function
        """
        this space is private, so is the variables 
        """
        return x + 1
    return bar(y * 2)

def bar(x):
    """
    x, y: int or float
    returns evaluation of private function
    Note: private function variables are private to it!!!
    """
    def foo(z, x = 0):#private function
        """
        this space is private, so is the variables 
        """
        return z + x
    return foo(3, x)

def foor(x):
    """
    x, y: int or float
    returns evaluation of private function
    Note: private function variables are private to it!!!
    """
    def barr(z, x = 0):#private function
        """
        this space is private, so is the variables 
        """
        return x + z
    return barr(3)

def square(x):
    """
    x: int or float
    returns square of x
    """
    return x*x

def fourthSquare(x):
    """
    x : int or float
    returns fourth power of x
    """
    return square(square(x))

def odd(x):
    """
    x : int
    return : True if x is odd, False otherwise
    """
    return (x % 2 == 1)
