#!/usr/bin/env python
# _*_ coding: utf-8 _*_



def is_palindrome_num(n):
    """
    >>> is_palindrome_num(1221)
    True
    >>> is_palindrome_num(1234)
    False
    """
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


def largest_palindrome(start, end):
    max_palindrome = 9009
    for i in range(start, end+1):
        for j in range(start, end+1):
            tmp = i * j
            if is_palindrome_num(tmp) and tmp > max_palindrome:
                max_palindrome = tmp
    return max_palindrome


if __name__ == '__main__':
    print largest_palindrome(100, 999)
