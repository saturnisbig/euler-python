#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

Costs: 2015-02-13 22:04:24 - 2015-02-13 22:36:14
"""


def is_palindromic(n):
    return True if n[::] == n[::-1] else False


def int_to_binary(n):
    """
    >>> int_to_binary(5)
    '101'
    >>> int_to_binary(9)
    '1001'
    >>> int_to_binary(1)
    '1'
    >>> int_to_binary(2)
    '10'
    """
    result = [n % 2]
    while True:
        r = int(n / 2)
        if r == 0:
            break
        result.append(r % 2)
        n = r
    result = map(str, result)
    return ''.join(result[::-1])


def get_result():
    result = 0
    for i in xrange(1, 1000000):
        i_bin = int_to_binary(i)
        if is_palindromic(str(i)) and is_palindromic(i_bin):
            result += i
    print result
    return result

if __name__ == '__main__':
    #print int_to_binary(2)
    get_result()
