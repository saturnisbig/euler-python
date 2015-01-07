#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem 14:
The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

Costs: 2015-01-07 19:45:06 - 2015-01-07 20:22:39
"""

result = {}

def collatz_sequence_cached(n):
    a = n
    if n in result:
        return result[n]
    else:
        counter = 1
        while True:
            if n == 1:
                break
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            if n in result:
                counter += result[n]
                break
            counter += 1
        result[a] = counter
    return counter


def collatz_sequence(n):
    counter = 1
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        counter += 1
    return counter


def largest_sequence_under(n):
    largest_seq = (1, 1)
    for i in range(1, n+1):
        # cached version costs 2 secs, while the other costs 25 secs.
        tmp = collatz_sequence_cached(i)
        if tmp > largest_seq[0]:
            largest_seq = (tmp, i)
    return largest_seq


if __name__ == '__main__':
    #print largest_sequence_under(5)
    import time
    start = time.time()
    result = largest_sequence_under(1000000)
    print 'Costs: ', time.time() - start, 'Result: ', result

