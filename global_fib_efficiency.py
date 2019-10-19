# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:41:08 2019

@author: HP
"""

#Tracking efficiency - fibonacci and globals

def fib(n):
    global numCalls
    numCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
def fib_eff(n, d):
    global numCalls
    numCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_eff(n-1, d) + fib_eff(n-2, d)
        d[n]=  ans
        return ans
    

n = 20

numCalls = 0
print(fib(n))
print("Ineff calls", numCalls)

numCalls = 0
d = {1:1, 2:2}
print(fib_eff(n, d))
print("Eff calls", numCalls)
