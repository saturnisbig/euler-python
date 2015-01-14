#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem:
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

Costs: 2015-01-13 20:56:19 - 2015-01-13 22:15:55
"""


words_dict = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
    12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety'
}


def less_than_100(n):
    words_list = []
    if n in words_dict:
        words_list.append(words_dict.get(n))
        return words_list
    else:
        t, g = n / 10, n % 10
        if t >= 2:
            words_list.append(words_dict.get(t * 10, ''))
        words_list.append(words_dict.get(g, ''))
        return words_list


def less_than_1000(n):
    if n < 100:
        return less_than_100(n)
    elif n < 1000:
        result = []
        hun = n / 100
        result.append(words_dict.get(hun))
        result.append('hundred')
        if n % 100:
            result.append('and')
            result.extend(less_than_100(n % 100))
        return result
    else:
        return ['one', 'thousand']


def number_to_words(n):
    return less_than_1000(n)


def words_of_numbers_under(n):
    for i in xrange(1, n+1):
        words = number_to_words(i)
        result = sum(map(len, words))
    return result, words


if __name__ == '__main__':
    #print words_of_numbers_under(1000)
    result = 0
    #print words_of_numbers_under(115)  # 20
    #print words_of_numbers_under(342)  # 23
    for i in range(1, 1001):
        result += words_of_numbers_under(i)[0]
    #    #print words_of_numbers_under(i)
    print result
