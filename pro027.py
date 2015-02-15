#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem 27:
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80
primes for the consecutive values n = 0 to 79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the
quadratic expression that produces the maximum number of
primes for consecutive values of n, starting with n = 0.

Costs: 2015-02-15 21:58:12 - 2015-02-15 22:10:48
"""


def is_prime(num):
    """
    see problem 3
    """
    if num < 2: 
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    # ignore even numbers
    for i in range(3, int(num**0.5+1), 2):
        if num % i == 0:
            return False
    return True


def get_result():
    result = (0, 0, 0)
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while True:
                tmp = n**2 + a * n + b
                if not is_prime(tmp):
                    break
                n += 1
            if n > result[0]:
                result = (n, a, b)
    print result[1] * result[2]
    return result


if __name__ == '__main__':
    print get_result()
