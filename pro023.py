#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

Costs: 2015-02-03 19:08:43 - 2015-02-03 19:23:43
       2015-02-11 22:15:02 - 2015-02-11 22:39:09
"""


def factors(n):
    """
    >>> factors(1)
    [1]
    >>> factors(6)
    [1, 2, 3]
    >>> factors(4)
    [1, 2]
    """
    result = [1]
    if n == 1:
        return result
    mid = int(n**0.5) + 1
    for i in xrange(2, mid):
        if n % i == 0:
            result.append(i)
            if n/i not in result:
                result.append(n/i)
    return result


def get_abundant_number(n):
    """
    >>> get_abundant_number(13)
    [12]
    """
    result = []
    for i in xrange(1, n+1):
        if i < sum(factors(i)):
            result.append(i)
    return result


def get_result():
    abundant_num = get_abundant_number(28123)
    abundant_num_sum = 0
    result = set()
    for i, n in enumerate(abundant_num):
        for j in abundant_num[i:]:
            tmp = n + j
            if tmp > 28123:
                break
            if tmp <= 28123 and tmp not in result:
            #else:
                abundant_num_sum += tmp
                result.add(tmp)
    print sum(range(1, 28124)) - abundant_num_sum  #sum(result)

def get_non_abundant_sums(limit):
    result = 0
    abundant_num = set()
    for i in xrange(1, limit):
        if sum(factors(i)) > i:
            abundant_num.add(i)
        if not any(i-a in abundant_num for a in abundant_num):
            result += i
    print result
    return result


if __name__ == '__main__':
    #get_non_abundant_sums(28124)
    #print get_abundant_number(100)
    get_result()
    #print factors(28122)
