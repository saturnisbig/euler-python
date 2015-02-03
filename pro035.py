#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?

Costs: 2015-02-03 22:26:56 - 2015-02-03 22:55:18
"""

def is_prime(num):
    """
    >>> is_prime(2)
    True
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(13)
    True
    >>> is_prime(15)
    False
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

def rotate_of_number(n):
    """
    >>> rotate_of_number(197)
    [971, 719, 197]
    >>> rotate_of_number(2)
    [2]
    >>> rotate_of_number(13)
    [31, 13]
    """
    result = []
    n_s = str(n)
    n_s_l = len(n_s)
    if n_s_l == 1:
        return [n]
    if n_s_l >= 2:
        for i in range(n_s_l):
            tmp = []
            for j in range(i+1, n_s_l):
                tmp.append(n_s[j])
            for k in range(i+1):
                tmp.append(n_s[k])
            result.append(int(''.join(tmp)))
    return result


def is_rotate_number_prime(n):
    rotates = rotate_of_number(n)
    l = map(is_prime, rotates)
    if False in l:
        return False
    else:
        return True


def get_circular_primes(n):
    # 2 is circular prime.
    counter = 1
    for i in xrange(3, n, 2):
        if is_prime(i) and is_rotate_number_prime(i):
            counter += 1
    return counter


if __name__ == '__main__':
    print get_circular_primes(1000000)
