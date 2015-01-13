#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem:
Find the sum of the digits in the number 100!
"""


def factors(n):
    if n == 1:
        return n
    else:
        return n * factors(n-1)


def sum_of_factors(n):
    return sum([int(c) for c in str(factors(n)) if c.isdigit()])


if __name__ == '__main__':
    print sum_of_factors(100)
