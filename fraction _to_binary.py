# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:52:07 2019

@author: Patrick
"""
#a pretty complex code ahead
x = 0.1#fraction
p = 0 #power

while((2**p)*x)%1 != 0: #whole number mod 1 is 0
    p+=1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2
    
for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]

print("The binary rep of", x, "is", '0'+result)
    
    
