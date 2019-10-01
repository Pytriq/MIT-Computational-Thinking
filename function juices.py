# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:46:45 2019

@author: Patrick
"""

def a(x, y, z):
    if x:
        return y
    else:
        return z

def b(x, y):
    return a(x > y, x, y)

def funFunc(x):
    x = x + 1
    def privateOps(y):
        return x + y
    return privateOps(7)

def cat():
    print("This is a cat")

def dog():
    print("I got a dog")

#uses
functionStore = a(False, cat, dog)
#type functionStore() on the console to see the magic

check = funFunc(45)
print(check)
