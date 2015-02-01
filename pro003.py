#!/usr/bin/env python
# _*_ coding: utf-8 _*_


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

def factors(num):
    """
    >>> factors(2)
    []
    >>> factors(4)
    [2, 2]
    >>> factors(5)
    []
    >>> factors(8)
    [2, 4]
    """
    #result = [1, num]
    result = []
    mid = int(num**0.5+1)
    i = 2
    while i < mid:
        if num % i == 0:
            result.append(i)
            result.append(num / i)
        i += 1
    #print result
    return result


def largest_prime_factor(num):
    prime_factors = [n for n in factors(num) if is_prime(n)]
    print prime_factors
    return max(prime_factors)


if __name__ == '__main__':
    #factors(6)
    #factors(5)
    #factors(12)
    print largest_prime_factor(600851475143)
    print largest_prime_factor(13195)
    #print is_prime(2639)
    #print is_prime(3)
    #print is_prime(11111111)
