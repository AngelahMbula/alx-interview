#!/usr/bin/python3
'''
Function returns list of int rep Pascal triangle
'''
from math import factorial


def pascal_triangle(n):
    '''
    Returns a list of intergers
    '''
    if n <= 0:
        return []
    for i in range(n):
        for j in range(n-i+1):
            
            # for left spacing
            print(end=" ")
            
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
            
        print()
