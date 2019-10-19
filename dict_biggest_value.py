# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:15:41 2019

@author: Patrick
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values          associated with it
    '''
    # Your Code Here
    big = 0
    result = None
    for key in aDict.keys():
        if len(aDict[key]) >= big:
            big = len(aDict[key])
            result = key
    return result 
    #or
    return max((len(v), k) for k, v in aDict.items())[1]
    #or
    return max(aDict.items(), key=lambda x: len(x[1]))[0]
    
