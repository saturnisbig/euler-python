#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem:
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

Costs: 2015-01-20 22:05:57 - 
"""

def maximum_path_sum(l):
    i = len(l) - 1
    while i > 0:
        for j in range(len(l[i])-1):
            tmp1 = l[i][j] + l[i-1][j]
            tmp2 = l[i][j+1] + l[i-1][j]
            if tmp1 > tmp2:
                l[i-1][j] = tmp1
            else:
                l[i-1][j] = tmp2
        i -= 1
    return l[0][0]


def find_max_sum():
    l = []
    with open('p067_triangle.txt', 'r') as fh:
        for line in fh:
            tmp = [int(c) for c in line.split()]
            l.append(tmp)
    print maximum_path_sum(l)



if __name__ == '__main__':
    find_max_sum()
