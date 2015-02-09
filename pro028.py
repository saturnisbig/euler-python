#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem:
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Costs: 2015-02-09 22:40:43 - 2015-02-09 22:56:14
思路：其实就是发现了以下规律，1;1+2,1+2+2,1+2+2+2,1+2+2+2+2; 9+1*4,9+2*4...
每次都是四个数，按2-4-6-8递增。
"""


def get_number_spiral(n):
    result = [1]
    counter = 1
    starter = 2
    while True:
        if counter > n:
            break
        for j in range(4):
            counter += starter
            if counter > n:
                break
            result.append(counter)
        starter += 2
    return result

def get_number_spiral_iter(n):
    counter = 1
    starter = 2
    yield counter
    while True:
        if counter > n:
            break
        for i in range(4):
            counter += starter
            if counter > n:
                break
            yield counter
        starter += 2

def find_result():
    print sum(get_number_spiral_iter(1001*1001))

if __name__ == '__main__':
    print sum(get_number_spiral(1001*1001))
    find_result()
