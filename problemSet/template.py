"""
Codeforces Round #334 (Div. 2)

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
    ...


# def pp(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    a, b, c = map(int, input().split())
    xs = [int(c) for c in input().split()]
    pairs = [tuple(map(int, input().split())) for _ in range(n)]
    assert len(xs) == n
    result = solve(xs, n)
    print(result)


if __name__ == '__main__':
    main()
