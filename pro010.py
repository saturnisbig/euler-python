#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Method: Find prime numbers that below two million, add all.
Cost: 2015-01-02 11:26:37 - 
"""
import time


def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    # ignore even numbers
    for i in range(3, int(num**0.5+1), 2):
        if num % i == 0:
            return False
    return True


def sum_of_primes_below(n):
    result = 2
    start = 3
    while True:
        if start >= n:
            break
        if is_prime(start):
            result += start
        start += 2
    return result


if __name__ == '__main__':
    start = time.time()
    print sum_of_primes_below(2000000)
    cost = time.time() - start
    print "Time Costs:", cost, " seconds."
