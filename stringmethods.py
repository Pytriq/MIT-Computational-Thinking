# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:19:48 2019

@author: Patrick
"""
#strings are immutable i.e. they can't be changed after 
#they're created

str1 = 'exterminate!'
str1.upper()#EXTERMINATE!
str1.capitalize #returns function
str2  = str1.capitalize() #Exterminate!
str2.swapcase() #eXTERMINATE!
str2.casefold()#converts everyhting to lowercase, #exterminate!
str2.lower() # exterminate!
str2.find('e') #0
str2.find('p') #-1 there's no p in exterminate
str2.find('T') #-1
str2.index('m') #5
str3 = str2.replace('!', 'r')#str3 = Exterminater
str3.count('e') #3
str1.islower()#True
str2.isupper()#False
str4 = str3.replace('r', '1')#NB replace takes strings only
str4.isalnum() #True




