"""
Date : 09/14/2023
Author : Dhriti Shah 
Assignment : Assignment 1

"""

def classify_triangle(a, b, c):

    ''' This function returns a string with the type of triangle from three  values'''
    if is_invalid(a, b, c):
        return "Invalid"
    if not is_triangle(a, b, c):
        return "Not a Triangle"
    if is_equilateral(a, b, c):
        return "Equilateral"
    if is_isosceles(a, b, c):
        return "Isosceles"
    if is_right(a, b, c):
        return "Right"
    return "Scalene"

def is_invalid(a, b, c):

    ''' This function returns True if the triangle is invalid'''
    if(a <= 0 or b <= 0 or c <= 0):
        return True
    if(a > 200 or b > 200 or c > 200):
        return True
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        return True
    return False

def is_triangle(a, b, c):
    ''' This function returns True if the triangle is valid'''
    if(a + b <= c or a + c <= b or b + c <= a):
        return False
    return True

def is_equilateral(a, b, c):
    ''' This function returns True if the triangle is equilateral'''
    if(a == b and b == c):
        return True
    return False

def is_isosceles(a, b, c):
    ''' This function returns True if the triangle is isosceles'''
    if(a == b or a == c or b == c):
        return True
    return False

def is_right(a, b, c):
    ''' This function returns True if the triangle is right'''
    if(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
        return True
    return False

def is_scalene(a, b, c):
    ''' This function returns True if the triangle is scalene'''
    if(a != b and a != c and b != c):
        return True
    return False

if __name__ == '__main__':
    print('classify_triangle(3, 3, 2) = ' + classify_triangle(3, 3, 2))
    print('classify_triangle(3, 3, 3) = ' + classify_triangle(3, 3, 3))
    print('classify_triangle(3, 4, 5) = ' + classify_triangle(3, 4, 5))
    print('classify_triangle(4, 5, 7) = ' + classify_triangle(4, 5, 7))
    print('classify_triangle(0, 3, 7) = ' + classify_triangle(0, 3, 7))
