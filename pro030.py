#!/usr/bin/env python
# _*_ coding: utf-8 _*_


"""
Problem:
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

Costs: 2015-02-01 16:49:40 - 2015-02-01 16:06:44
In case I forgot: 9^5 * 7 = 59049 * 7 = 413343 < 1000000, so find number less
than 1000000. In the begin, I thought I just need to find the 5-digits numbers
whose sum of fifth powers of their digits equal to themself.
"""


def get_sum_of_fifth_powers_digits():
    result = []
    for n in xrange(2, 1000000):
        digits = [int(c)**5 for c in str(n)]
        if sum(digits) == n:
            result.append(n)
    print result
    return result


if __name__ == '__main__':
    print sum(get_sum_of_fifth_powers_digits())
