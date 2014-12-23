#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def sum_square_difference(num):
    square_of_sum = sum(range(1, num+1))**2
    sum_of_square = sum([i*i for i in range(1, num+1)])
    print square_of_sum, sum_of_square
    return square_of_sum - sum_of_square


if __name__ == '__main__':
    print sum_square_difference(100)
