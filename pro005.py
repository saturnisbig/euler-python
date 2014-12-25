#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
date: 2014-12-25 14:12:37 to 2014-12-25 14:38:41

"""

def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(r, b)


def smallest_multiple(n):
    l = [i for i in range(1, n+1)]
    for i in range(n-1):
        l[i+1] = (l[i] * l[i+1]) / gcd(l[i], l[i+1])
    print l
    return l[-1]


def smallest_multiple_v2(n):
    l = [i for i in range(1, n+1)]
    return reduce(lambda a, b: (a*b)/gcd(a, b), l)

if __name__ == '__main__':
    #print gcd(19, 4)
    #print gcd(3, 2)
    print smallest_multiple_v2(10)
    print smallest_multiple(20)
