# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:42:27 2019

@author: HP
"""

def isPal(x):
    '''
    x : list
    returns true if x is a palindrome
    '''
    assert type(x) == list
    
    temp = x.copy()#very important to copy x
    temp.reverse()
    
    if temp == x:
        return True
    else:
        return False
    
def silly(n):
    '''
    n: integer
    returns yes, if enter chars make a palindrom
    '''
    result = []
    for i in range(n):
        char = input("Enter a character: ")
        result.append(char.lower())
        
    if isPal(result):
        print("Yes")
    else:
        print("No!")
        
    