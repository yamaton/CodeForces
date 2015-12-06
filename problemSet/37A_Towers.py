"""
Codeforces Round

Problem 37 A. Towers

@author yamaton
@date 2015-12-01
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs, n):
    d = collections.Counter(xs)
    return max(d.values()), len(d)


# def pp(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(c) for c in input().split()]
    assert len(xs) == n
    result = solve(xs, n)
    print(*result)


if __name__ == '__main__':
    main()
