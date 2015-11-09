"""
Codeforces Round #327 (Div. 2)

Problem 591 A. Wizards' Duel

@author yamaton
@date 2015-11-06
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(l, p, q):
    return l * p / (p + q)


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    l = int(input())
    p = int(input())
    q = int(input())
    result = solve(l, p, q)
    print(result)


if __name__ == '__main__':
    main()
