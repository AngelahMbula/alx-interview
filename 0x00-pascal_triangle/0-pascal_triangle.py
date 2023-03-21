#!/usr/bin/python3
def pascal_triangle(n):
    from math import factorial
    if n <= 0:
        return []
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()
