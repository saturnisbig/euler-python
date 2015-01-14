#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
The 12th term, F12, is the first term to contain three digits.
Whatt is the first term in the Fibonacci sequence to contain 1000 digits?
"""


def fib_iter():
    n1, n2 = 1, 1
    counter = 1
    while True:
        yield n1, counter
        n1, n2 = n2, n1 + n2
        counter += 1

def get_n_digits_fib(n):
    result = 1
    for num, counter in fib_iter():
        if len(str(num)) >= n:
            result = num, counter
            break
    return result


if __name__ == '__main__':
    print get_n_digits_fib(1000)
