# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:58:21 2019

@author: Patrick
"""

ans = 0
neg_flag = False
x = int(input("Enter a number to square:"))

if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("The squareroot of", x, "is", ans )
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking...did you mean", -x,"?")
