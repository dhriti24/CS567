"""
Date : 09/14/2023
Author : Dhriti Shah 
Assignment : Assignment 1

"""

def classify_triangle(a, b, c):
    #ToDO
    if(isInvalid(a, b, c)):
        return "Invalid"
    elif(not(isTriangle(a, b, c))):
        return "Not a Triangle"
    elif(isEquilateral(a, b, c)):
        return "Equilateral"
    elif(isIsosceles(a, b, c)):
        return "Isosceles"
    elif(isRight(a, b, c)):
        return "Right"
    else:
        return "Scalene"

def isInvalid(a, b, c):
    if(a <= 0 or b <= 0 or c <= 0):
        return True
    if(a > 200 or b > 200 or c > 200):
        return True
    if(not(isinstance(a, int)) or not(isinstance(b, int)) or not(isinstance(c, int))):
        return True
    else:
        return False
    
def isTriangle(a, b, c):
    if(a + b <= c or a + c <= b or b + c <= a):
        return False
    else:
        return True
    
def isEquilateral(a, b, c):
    if(a == b and b == c):
        return True
    else:
        return False
    
def isIsosceles(a, b, c):
    if(a == b or a == c or b == c):
        return True
    else:
        return False
    
def isRight(a, b, c):
    if(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
        return True
    else:
        return False
    
def isScalene(a, b, c):
    if(a != b and a != c and b != c):
        return True
    else:
        return False
    
if __name__ == '__main__':
    print('classify_triangle(3, 3, 2) = ' + classify_triangle(3, 3, 2))
    print('classify_triangle(3, 3, 3) = ' + classify_triangle(3, 3, 3))
    print('classify_triangle(3, 4, 5) = ' + classify_triangle(3, 4, 5))
    print('classify_triangle(4, 5, 7) = ' + classify_triangle(4, 5, 7))
    print('classify_triangle(0, 3, 7) = ' + classify_triangle(0, 3, 7))
