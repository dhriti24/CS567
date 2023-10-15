"""
Date : 09/22/2023
Author : Dhriti Shah 
Assignment : Assignment 2a

"""
from check_triangle import classify_triangle

def test_invalid_input():
    ''' This function tests the invalid inputs'''
    assert classify_triangle(2000, 3000, 4000) == 'InvalidInput'
    assert classify_triangle(1, 1.1, 1) == 'InvalidInput'
    assert classify_triangle(-1, 1, 1) == 'InvalidInput'

def test_not_a_triangle():
    ''' This function tests the NotATriangle'''
    assert classify_triangle(1, 1, 3) == 'NotATriangle'
    assert classify_triangle(6, 6, 14) == 'NotATriangle'
    assert classify_triangle(3, 4, 9) == 'NotATriangle'

def test_equilateral():
    ''' This function tests the Equilateral'''
    assert classify_triangle(1, 1, 1) == 'Equilateral'
    assert classify_triangle(100, 100, 100) == 'Equilateral'
    assert classify_triangle(200, 100, 200) != 'Equilateral'

def test_right():
    ''' This function tests the Right'''
    assert classify_triangle(3, 4, 5) == 'Right'
    assert classify_triangle(8, 6, 10) == 'Right'
    assert classify_triangle(4, 5, 6) != 'Right'

def test_isoceles():
    ''' This function tests the Isoceles'''
    assert classify_triangle(2, 1, 2) == 'Isoceles'
    assert classify_triangle(3, 3, 5) == 'Isoceles'
    assert classify_triangle(2, 3, 1) != 'Isoceles'

def test_scalene():
    ''' This function tests the Scalene'''
    assert classify_triangle(4, 2, 3) == 'Scalene'
    assert classify_triangle(6, 8, 12) == 'Scalene'
    assert classify_triangle(3, 2, 3) != 'Scalene'
