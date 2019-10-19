# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:08:41 2019

@author: HP
"""
#tuples

#define a tuple
marks = ()
marks = (2,4,5)

#a tuple with one item
tup1 = (1,) #the comma is a must

#swap two value without using temp
#(x,y) = (y,x)

def quotientAndRemainder(x,y):
    quot = x//y
    rem = x%y
    
    return (quot, rem)

#quotientAndRemainder(20,6)

#q,r = quotientAndRemainder(20,6)
    
def getData(aTuple):
    """
    aTuple : a tuple of tuples with nums and strs
    returns min and max number, a number of unique words
    as a tuple
    """
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)#comma to return a tuple not int 
        if t[1] not in words:
            words = words + (t[1],)
            
    minNum = min(nums)
    maxNum = max(nums)
    uniqueWords = len(words)
    
    return (minNum, maxNum, uniqueWords)

#tupl = ((4,"four"), (9,"nine"), (9,"nine"), (5,"five"))          
    

def oddTuples(tup):
    """
    tup : tuple
    return every other element of tup
    """
    return tup[::2]

def intersect(t1, t2):
    """
    iterating in tuples
    t1 and t2: tuples
    returns values that a both in t1 and t2
    """
    common = ()
    for n in t1:
        if n in t2:
            common += (n,)
    return common
            
def minMaxDivisor(n1, n2):
    """
    n1 and n2: int > 1
    returns minimum and maximum divisor of n1 and n2, tuple,
    otherwise return None, None
    """
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return (minVal, maxVal)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

