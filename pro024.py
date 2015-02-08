#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem:
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

   012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?

Costs: 2015-02-01 12:49:27 - 2015-02-01 13:17:49
       2015-02-01 15:39:47 - 
"""


def facs(n):
    return reduce(lambda a, b: a*b, range(1, n+1), 1)


def get_permutation_3(l):
    return [[l[0], l[1], l[2]], [l[0], l[2], l[1]], [l[1], l[0], l[2]],
            [l[1], l[2], l[0]], [l[2], l[0], l[1]], [l[2], l[1], l[0]]]

def permutation(n):
    l = range(10)
    result = []

    for i in range(10):
        counter = 0
        while True:
            if n >= facs(9-i):
                counter += 1
                n -= facs(9-i)
                #print i, n
            else:
                if counter > 0 and n > 0:
                    result.append(l.pop(counter))
                else:
                    #print get_permutation_3(l)
                    result.extend(get_permutation_3(l)[counter*facs(9-i)-1])
                break
        if n == 0:
            break
    return ''.join(map(str, result))


if __name__ == '__main__':
    print permutation(1000000)
    print get_permutation_3([0, 4, 6])[3]
