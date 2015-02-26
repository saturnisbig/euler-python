#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem 26:
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.

Costs: 2015-02-26 19:12:06 - 2015-02-26 19:42:51
"""

def get_cycle(n):
    """
    >>> get_cycle(3)
    (3, 1)
    >>> get_cycle(6)
    (6, 1)
    >>> get_cycle(7)
    (7, 6)
    >>> get_cycle(17)
    (17, 16)
    >>> get_cycle(81)
    (81, 9)
    >>> get_cycle(2)
    (2, 0)
    >>> get_cycle(9)
    (9, 1)
    """
    power = 10**len(str(n))
    starter = 1 * power
    tmp1 = []
    counter = 0
    while True:
        r = starter % n
        if r == 0:
            break
        if r not in tmp1:
            tmp1.append(r)
            counter += 1
            # 将余数乘10，按照除法的法则
            starter = r * 10
        else:
            cycle_start = tmp1.index(r)
            if cycle_start > 0:
                counter = len(tmp1) - cycle_start - 1
            break
    return n, counter


def get_longest_cycle(n):
    result = (0, 0)
    for i in xrange(2, n):
        tmp = get_cycle(i)
        if tmp[1] > result[1]:
            result = tmp
    return result


if __name__ == '__main__':
    print get_longest_cycle(1000)
