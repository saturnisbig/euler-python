#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem 16:

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?

Costs: 2015-01-05 19:48:37 - 2015-01-05 19:49:11
"""


def power_digit_sum(num, power):
    return sum(int(digit) for digit in str(num**power))


if __name__ == '__main__':
    print power_digit_sum(2, 1000)
