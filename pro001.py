#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# Problem 1
# If we list all the natural numbers below 10 that are multiples of
# 3 or 5, we get 3, 5, 6, 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def find_multiples(max_num):
    """
    >>> find_multiples(10)
    23
    >>> find_multiples(3)
    0
    >>> find_multiples(5)
    3
    """
    result = []
    for i in range(1, max_num):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)
    return sum(result)

print find_multiples(1000)
