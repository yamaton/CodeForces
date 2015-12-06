"""
Codeforces Round

Problem 1 B. Spreadsheets

@author yamaton
@date 2015-12-01
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def int_to_alph(n):
    ...


def excel_to_rc(s):
    row, col = (''.join(iterable) for (_, iterable) in it.groupby(s, str.isalpha))


def rc_to_excel(s):
    _, row, _, col = (''.join(iterable) for (_, iterable) in it.groupby(s, str.isalpha))
    ...


def is_excel_style(s):
    return sum(1 for _ in it.groupby(s, str.isalpha)) == 2

def convert(s):
    if is_excel_style(s):
        return excel_to_rc(s)
    else:
        return rc_to_excel(s)


# def pp(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    ss = [input() for _ in range(n)]
    for s in ss:
        res = solve(s)
        print(result)


if __name__ == '__main__':
    main()
