#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

a = m^2 - n ^2, b = 2mn, c = m^2 + n^2
a+b+c=2m(m+n)=1000
m(m+n)=500，通过循环获取上述乘积中m和n的值
参考材料：https://projecteuler.net/thread=9
"""

def find_special_pythagorean_triplet():
    result = 0
    for i in range(1, 500):
        if 500 % i == 0:
            m = i
            n = 500 / i - i
            if m > n and n > 0:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                result = a * b * c
                print a, b, c, result
    return result


if __name__ == '__main__':
    find_special_pythagorean_triplet()

