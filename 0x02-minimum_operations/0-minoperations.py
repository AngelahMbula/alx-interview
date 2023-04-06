#!/usr/bin/python3
"""contains the minOperations method"""


def minOperations(n):
    """return: Returns an integer."""
    if not isinstance(n, int) or n <= 1:
        return 0

    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i += 1
    return sum(factors)
