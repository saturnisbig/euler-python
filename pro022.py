#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Costs: 2015-01-26 08:53:40 - 2015-01-26 14:17:08
"""


def first_name_sorted_alph():
    with open('p022_names.txt', 'r') as fh:
        for line in fh:
            tmp = line.split(',')
    result = [eval(s) for s in tmp]
    return sorted(result)


def name_scores(name, pos):
    # A -> 1, B -> 2, start from 1
    intA = ord('A') - 1
    score = map(ord, name)
    score = [i-intA for i in score]
    return sum(score) * pos

def names_scores(l):
    result = 0
    for i, name in enumerate(l):
        score = name_scores(name, i+1)
        result += score
        #if name == 'COLIN':
        #    print i+1, name
        #    break
    return result


if __name__ == '__main__':
    print first_name_sorted_alph()[0]
    l = first_name_sorted_alph()
    print name_scores('COLIN', 938)
    print names_scores(l)
