#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Costs: 2015-01-26 08:29:57 - 2015-01-26 08:47:40
"""


def factors(n):
    result = [1,]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            result.append(i)
            result.append(n/i)
    return result


def is_amicable_number(n):
    dn = sum(factors(n))
    if sum(factors(dn)) == n and dn != n:
        return (True, dn)
    else:
        return (False, 0)


def amicable_number_sum(n):
    result = []
    for i in range(1, n+1):
        is_amicable = is_amicable_number(i)
        if is_amicable[0] and i not in result:
            result.append(i)
            if is_amicable[1] not in result:
                result.append(is_amicable[1])
    return result


if __name__ == '__main__':
    print sum(factors(220))
    print is_amicable_number(220)
    print sum(amicable_number_sum(10000))
