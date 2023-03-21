#!/usr/bin/python3
from math import factorial


def pascal_triangle(n):
    '''
    returns list of integers representing pascals triangle
    '''
    if n <= 0:
        return []
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()
