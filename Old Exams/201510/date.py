#! /usr/bin/env python3


def create_date(y, m, d):
    if m not in range(1, 13):
        raise ValueError('Invalid month {}'.format(m))

    if d not in range(1, days_in_month(y, m) + 1):
        raise ValueError('Invalid day {} for month {}'.format(d, m))

    return {'y': y, 'm': m, 'd': d}


def days_in_month(y, m):
    default = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = default[m - 1]

    if m == 2 and is_leap_year(y):
        days += 1

    return days


def is_leap_year(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


def day(date):
    return date['d']


def month(date):
    return date['m']


def year(date):
    return date['y']


def to_string(date):
    return '{y:04d}-{m:02d}-{d:02d}'.format(**date)


def to_date(string):
    import re
    if not re.match(r'\d{4}-\d{2}-\d{2}', string):
        raise ValueError(string + ' is not a valid date string')
    return create_date(*map(int, string.split('-')))


def next_date(y, m, d):
    if (d + 1) > days_in_month(y, m):
        if (m + 1) > 12:
            return create_date(y + 1, 1, 1)
        else:
            return create_date(y, m + 1, 1)
    else:
        return create_date(y, m, d + 1)
