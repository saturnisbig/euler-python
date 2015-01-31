#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
Problem:
You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September, April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Costs: 2015-01-31 10:20:42 - 2015-01-31 11:44:58
"""


def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def days_of_year(year):
    days_except_feb = 31+31+30+31+30+31+31+30+31+30+31
    if is_leap_year(year):
        return days_except_feb + 29
    else:
        return days_except_feb + 28


def days_since_1900(year, month, day):
    days = 0
    for y in xrange(1900, year):
        days += days_of_year(y)
    if month > 2:
        if is_leap_year(year):
            days += 29
        else:
            days += 28
    month_day_dict = {
        1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
        8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
    }
    for m in xrange(1, month):
        if m in month_day_dict:
            days += month_day_dict.get(m)
    return days + day - 1


def get_day_of_week(year, month, day):
    if year < 1900:
        return -1
    days = days_since_1900(year, month, day)
    return 1 + days % 7


def sundays(start_year, end_year):
    result = 0
    for y in xrange(start_year, end_year+1):
        for m in xrange(1, 13):
            d = get_day_of_week(y, m, 1)
            if d == 7:
                result += 1
    return result


if __name__ == '__main__':
    #print is_leap_year(2002)
    #print is_leap_year(1600)
    #print is_leap_year(2012)
    #print is_leap_year(100)
    #print get_day_of_week(2015, 1, 1)
    #print get_day_of_week(2015, 2, 1)
    #print get_day_of_week(1900, 1, 2) 
    print get_day_of_week(2015, 1, 30)
    print sundays(1901, 2000)
