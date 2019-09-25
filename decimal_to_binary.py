# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:23:09 2019

@author: Patrick
"""

num = 11
isNeg = False
result = ''

if num < 0:
    isNeg = True
    num = abs(num)
if num == 0:
    result = '0'

while num > 0:
    result = str(num%2) + result
    num = num // 2
if isNeg:
    result = '-'+ result
