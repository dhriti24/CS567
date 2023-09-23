"""
Date : 09/14/2023
Author : Dhriti Shah 
Assignment : Assignment 1

"""

from Triangle import classify_triangle

def test_invalid():
    test_value = 'Invalid'
    assert test_value == classify_triangle(0, 0, 0)
    assert test_value == classify_triangle(0, 0, 1)
    assert test_value != classify_triangle(4, 1, 7)

def test_not_a_triangle():
    test_value = 'Not a Triangle'
    assert test_value == classify_triangle(3, 3, 7)
    assert test_value == classify_triangle(3, 10, 7)
    assert test_value != classify_triangle(3, 3, 3)
    #assert test_value == classify_triangle(3, 3, 3)

def test_equilateral():
    test_value = 'Equilateral'
    assert test_value == classify_triangle(4, 4, 4)
    assert test_value == classify_triangle(3, 3, 3)
    assert test_value != classify_triangle(3, 3, 7)

def test_isosceles():
    test_value = 'Isosceles'
    assert test_value == classify_triangle(3, 3, 2)
    assert test_value == classify_triangle(3, 4, 3)
    assert test_value != classify_triangle(3, 4, 5)

def test_right():
    test_value = 'Right'
    assert test_value == classify_triangle(3, 4, 5)
    assert test_value == classify_triangle(5, 12, 13)
    assert test_value != classify_triangle(3, 3, 7)

def test_scalene():
    test_value = 'Scalene'
    assert test_value == classify_triangle(8, 4, 9)
    assert test_value == classify_triangle(3, 5, 7)
    assert test_value != classify_triangle(3, 3, 3)
    
