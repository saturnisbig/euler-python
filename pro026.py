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

def get_result(n):
    result = (0, 0)
    for i in xrange(2, n):
        power = 10**len(str(i))
        starter = 1 * power
        tmp1 = []
        counter = 0
        while True:
            r = starter % i
            if r == 0:
                break
            #d = int(starter / i)
            if r not in tmp1:
                tmp1.append(r)
                starter = r * power
                counter += 1
            else:
                break
            #print i, r
        if counter > result[0]:
            result = (counter, i)
    return result


if __name__ == '__main__':
    print get_result(1000)
