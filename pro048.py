#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem:
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

Costs: 2015-01-31 12:48:54 - 2015-01-31 12:52:43
"""


def get_sum_of_self_power(n):
    result = 0
    for i in xrange(1, n+1):
        result += i**i
    return result


if __name__ == '__main__':
    print str(get_sum_of_self_power(1000))[-10:]
