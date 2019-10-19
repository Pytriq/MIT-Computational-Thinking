# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:58:52 2019

@author: HP
"""
"""
Dicts 
- are muatable
- unordered
- keys must be hashable
- all immutables are hashable, mutables are not
"""



planets = {'Mercury':1, 'Venus':2, 'Earth':3, 'Mars':4,     'Jupiter':5, 'Saturn':6, 'Uranus':7, 'Neptune':8, 1:'Mercury',2:'Venus', 3:'Earth', 4:'Mars', 5:'Jupiter'}

print("The third planet from the sun is:", planets[3])
diff = planets['Jupiter'] - planets['Mercury']
print("Between Jup and Merc thre are", diff,"planets")

#add pluto

planets['Pluto'] = 9

planetNames = list(planets.keys())
planetPos = list(planets.values())

print(planetNames)

#scientificaly
del planets['Pluto']
print(planets)

#for p in planets: #iterates over the keys 

#'Pluto' in grades
animals = {'c':['cat','chicken','cheatah'], 'd':['dog','donkey','duck'],'b':['bat', 'beer']}

animals['b'].append('bee')

#count number of animals in animal dict

def animal_count(animals):
    """
    animals: a dictionary
    returns sum of number of values in the dictionary
    """
    result = 0
    for key in animals.keys():
        result += len(animals[key])
    return result

    #or
    for value in animals.values():
        result += len(value)
    return result

    #or
    for i in animals:
        result += len(animals[i])
        
    return result
    
    #or
    return sum(map(len, animals.values()))

    #or
    return sum([len(v) for v in animals.values()])




