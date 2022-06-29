import datetime as dt
import sys
FI = (5 ** 0.5 - 1) / 2


def calculate(a, d1, b, d2):
    if d1[0] == d2[0]:
        delta = dt.timedelta(abs((d2 - d1).days))
    elif a != 2:
        delta = dt.timedelta(abs((dt.date(9800, 1, 1) - d1[1]).days) + abs((d2[1] - dt.date(1, 1, 1).days)))
    else:
        delta = dt.timedelta(abs((dt.date(9800, 1, 1) - d2[1]).days) + abs((d1[1] - dt.date(1, 1, 1).days)))
    sp = [0, 0, 0, 0]
    sp[a - 1] = d1
    sp[b - 1] = d2
    if a == 1 and b == 2:
        d = dt.timedelta(round(FI * delta.days))
        sp[3] = sum_date(sp[0], d, '+')
        sp[2] = sum_date(sp[1], d, '-')
    elif a == 1 and b == 3:
        d = dt.timedelta(round(delta.days / (1 - FI)))
        sp[1] = sum_date(sp[0], d, '+')
        sp[3] = sum_date(sp[1], delta, '-')
    elif a == 1 and b == 4:
        d = dt.timedelta(round(delta.days / FI))
        sp[1] = sum_date(sp[0], d, '+')
        sp[2] = sum_date(sp[1], delta, '-')
    elif a == 2 and b == 3:
        d = dt.timedelta(round(delta.days / FI))
        sp[0] = sum_date(sp[1], d, '-')
        sp[3] = sum_date(sp[0], delta, '+')
    elif a == 2 and b == 4:
        d = dt.timedelta(round(delta.days / (1 - FI)))
        sp[0] = sum_date(sp[1], d, '-')
        sp[2] = sum_date(sp[0], delta, '+')
    elif a == 3 and b == 4:
        d = dt.timedelta(round(delta.days * (1 - FI) / (2 * FI - 1)))
        sp[0] = sum_date(sp[2], d, '-')
        sp[1] = sum_date(sp[3], d, '+')
    return sp


def check(d, m, y):
    if y == '' or not (y.isdigit() or (y[0] == '-' and y[1:].isdigit())):
        return -1
    y = int(y)
    if y == 0:
        return -1
    if (d == 31 and m in [2, 4, 6, 9, 11]) or (d == 30 and m == 2):
        return -1
    if m == 2 and d == 29 and not ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        return -1
    return 0

def age(d1, d2):
    if d1[0] == d2[0]:
        m = (d2[1].year - d1[1].year) * 12 + (d2[1].month - d1[1].month)
    else:
        m = (d2[1].year - 1 + 9800 - d1[1].year) * 12 + (d2[1].month - d1[1].month)
    d = d2.day - d1.day
    if d < 0 and d1.month == 12:
        d += 31
        m -= 1
    elif d < 0:
        d += (dt.date(d1.year, d1.month + 1, 1) - dt.date(d1.year, d1.month, 1)).days
        m -=1
    y = m // 12
    m = m % 12
    
    return (d, m, y)


def check_time(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return -1
    if y1 == y2 and m2 < m1:
        return -1
    if y1 == y2 and m2 == m1 and d2 < d1:
        return -1
    return 0


def add_date(y, m, d):
    if y < 0:
        sp = [-1, dt.date(y + 9800, m, d)]
    else:
        sp = [0, dt.date(y, m, d)]
    return sp


def sum_date(date, delta, zn):
    if zn == '+':
        if date[0] == -1 and (dt.date(9800, 1, 1) - date[1]).days <= delta.days:
            res = [0, dt.date(1, 1, 1) + (delta - (dt.date(9800, 1, 1) - date[1]))]
        else:
            res = [date[0], date[1] + delta]
    else:
        if date[0] == 0 and (date[1] - dt.date(1, 1, 1)).days < dalta.days:
            res = [-1, dt.date(9800, 1, 1) - (delta - (date[1] - dt.date(1, 1, 1)))]
        else:
            res = [date[0], date[1] - delta]
    return res