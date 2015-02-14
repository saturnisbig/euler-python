#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Costs: 2015-02-14 10:52:32 - 2015-02-14 11:30:07
Reference: http://blog.csdn.net/no_end_point/article/details/4301149
找出上限然后用暴力分析法， 9!*n < 10^n
"""


def fact_index(i):
    fact_list = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return fact_list[i]


def get_limit():
    limit = 0
    n = 1
    while True:
        limit = 10**n
        if 362880*n < limit:
            break
        n += 1
    return limit


def is_curious_num(n):
    """
    >>> is_curious_num(145)
    True
    """
    i_digit_sum = 0
    tmp = n
    if n == 1 or n == 2:
        return False
    while tmp >= 10:
        i_digit_sum += fact_index(tmp % 10)
        tmp = tmp / 10
    i_digit_sum += fact_index(tmp)
    if i_digit_sum == n:
        return True
    else:
        return False


def get_result(limit):
    """
    >>> get_result(150)
    145
    """
    result = 0
    for i in xrange(10, limit):
        if is_curious_num(i):
            result += i
    #print result
    return result


if __name__ == '__main__':
    import time
    start = time.time()
    print get_result(get_limit())
    print "It takes: ", time.time() - start
    #get_result(150)
    #print get_limit()
