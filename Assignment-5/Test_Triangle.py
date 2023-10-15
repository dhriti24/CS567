"""
Date : 09/22/2023
Author : Dhriti Shah 
Assignment : Assignment 2a

"""
from Triangle import classifyTriangle

def test_invalid_input():
    assert classifyTriangle(2000, 3000, 4000) == 'InvalidInput'
    assert classifyTriangle(1, 1.1, 1) == 'InvalidInput'
    assert classifyTriangle(-1, 1, 1) == 'InvalidInput'

def test_not_a_triangle():
    assert classifyTriangle(1, 1, 3) == 'NotATriangle'
    assert classifyTriangle(6, 6, 14) == 'NotATriangle'
    assert classifyTriangle(3, 4, 9) == 'NotATriangle'

def test_equilateral():
    assert classifyTriangle(1, 1, 1) == 'Equilateral'
    assert classifyTriangle(100, 100, 100) == 'Equilateral'
    assert classifyTriangle(200, 100, 200) != 'Equilateral'

def test_right():
    assert classifyTriangle(3, 4, 5) == 'Right'
    assert classifyTriangle(8, 6, 10) == 'Right'
    assert classifyTriangle(4, 5, 6) != 'Right'

def test_isoceles():
    assert classifyTriangle(2, 1, 2) == 'Isoceles'
    assert classifyTriangle(3, 3, 5) == 'Isoceles'
    assert classifyTriangle(2, 3, 1) != 'Isoceles'

def test_scalene():
    assert classifyTriangle(4, 2, 3) == 'Scalene'
    assert classifyTriangle(6, 8, 12) == 'Scalene'
    assert classifyTriangle(3, 2, 3) != 'Scalene'