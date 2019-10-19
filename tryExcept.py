# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:52:23 2019

@author: HP
"""

def ratio():
    '''
    returns ration of two int or float values
    '''
    try:
        x = int(input("Enter first value: "))
        y = int(input("Enter seconds value: "))
        print("Perfect", round(x/y, 2))
    except ValueError:
        print("Please enter a float or int")
    except ZeroDivisionError:
        print("Sorry! Can't divide by zero")
    except:
        print("Something isn't right!!")
        
def enterInt():
    '''
    expects int from user
    exits when int is provided
    '''
    while True:
        try:
            n = input("Please enter an int: ")
            n = int(n)
            break
        except ValueError:
            print("Sorry! Did you enter an int?")
        except:
            print("Try entering an int! ")
    print("Good job")

def readFile():
    '''
    opens and reads a file, throws exception 
    '''
    data = []
    file = input("Enter name of file to open: ")
    try:
        f = open(file, 'r')
    #throw an exception if file not found
    except IOError:
        print("Cannot open", file)
    #else execute this code
    else:
        for new in f:
            if new != '\n':
                addIt = new[:-1].split(',')
                data.append(addIt)
        print(data)
    finally:
        f.close()
    grades = []
    if data:
        for student in data:
            try:
                
                name = student[:-1]# removes grade from list,
                grade = int(student[-1])
                grades.append([name, [grade]])
            except ValueError:
                grades.append([student[:],[]])
                
        print(grades)
            

#try testGrades.txt
            
def getRatios(l1, l2):
    '''
    l1,l2 : lists of equal length with numbers
    returns list containing l1[i]/l2[i]
    
    '''
    ratios = []
    for i in range(len(l1)):
        try:
            ratios.append(l1[i]/l2[i])
        except ZeroDivisionError:
            ratios.append(float('NaN'))#Not a number
        except:
            raise ValueError ('getRatios called with bad argument')
    return ratios 

def getStats(marks_list):
    '''
    marks_list: list with student names and marks
    returns: new list with student name, marks and average score
    '''
    new_list = []
    for item in marks_list:
        new_list.append([item[0], item[1], avg(item[1])])
    return new_list

def avg(x):
    '''
    x: list with float or int
    returns average of the values in the list
    '''
    try:
        return sum(x)/len(x)
    except ZeroDivisionError:
        print("student has no grades")
        return 0.0
    
test_marks = [[['Peter','Parker'], [75, 60.0, 35, 67]],
              [['John','Mujuu'],[45, 56, 89,1, 90]],
              [['James','Kamau'],[46,89,100,79.0]],
              [['Bill','Gates'],[]]
              ]

def fancy_divide(numbers, index):
    '''
    numbers: list of ints
    x: int
    returns 
    '''
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")
        
#fancy_divide([0, 2, 4], 4) - 100
#fancy_divide([0, 2, 4], 9) - 100
#fancy_divide([0, 2, 4], 2) - 10

def average(num_list):
    '''
    num_list: list of floats or ints or empty
    returns average of list items
    '''
    #assertions used to check type of argument or value
    #to check invariants on data structure are met
    #to check constraints on return values
    #to violation of constraints on procedure, e.g. no duplicates on list
    assert not len(num_list) == 0, 'No grades supplied'
    return sum(num_list)/len(num_list)

def number():
    '''
    checking the input type using assertion
    '''
    try:
        x = int(input("Enter a number: "))
        assert x >= 0, "Only positive numbers accepted"
        print(x)
    except AssertionError as msg:
        print(msg)
    except ValueError:
        print("Please enter an integer")
    except Exception as ex:
        print(ex)

def normalize(numbers):
    '''
    numbers: list of ints
    returns a list of each number over the max

    '''
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers
        
        


        
        
        
        
        
        
        
            
                
            
        