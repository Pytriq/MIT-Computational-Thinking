# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:06:15 2019

@author: HP
"""

#fibonacci using  dictionary, efficient

def fib_eff(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_eff(n-1, d) + fib_eff(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
#fib_eff(7,d)
