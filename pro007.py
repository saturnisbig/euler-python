#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    # ignore even numbers
    for i in range(3, int(num**0.5+1), 2):
        if num % i == 0:
            return False
    return True


def prime_iter(n):
    i = 2
    while True:
        if i < n:
            if is_prime(i):
                yield i
            i += 1
        else:
            break


def get_nth_prime(n):
    if n == 1:
        return 2
    i = 1
    start = 3
    result = 3
    while i < n:
        if is_prime(start):
            i += 1
            result = start
        start += 2
    return result


if __name__ == '__main__':
    print get_nth_prime(6)
    print get_nth_prime(10001)
