# -*- coding: utf-8 -*-
"""
Date : 09/22/2023
Author : Dhriti Shah 
Assignment : Assignment 2a

"""
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    # ERROR 1: b <= b should be b <= 0
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    # Error 2: a >= (b-c) or b >= (a-c) or c >= (a-b) should be (a + b <= c) or (a + c <= b) or (b + c <= a):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'
    # now we know that we have a valid triangle 
    # ERROR 3: a == b and b == a should be a == b and b == c
    if a == b and b == c:
        return 'Equilateral'
    # ERROR 4: b * 2 should be b * b and c * b should be c * c
    elif ((a * a) + (b * b)) == (c * c):
        return 'Right'
    elif (a != b) and  (b != c) and (c != a):
        return 'Scalene'
    # ERROR 5: a == b and b == a should be a == b or b == c or c == a
    elif (a == b) or (b == a) or (c == a):
        return 'Isoceles'
    else:
        return 'NotATriangle'
