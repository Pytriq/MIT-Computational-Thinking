# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:33:55 2019

@author: Patrick
"""

def is_even(param):
    """
    accepts one value as argument
    returns True if value is even 
    otherwise returns false
    """
    if param % 2 == 0:
        print(param, "is even")
    else:
        print(param, "is not even")
#    print("hi")
#    return param % 2 == 0

is_even(74)    
