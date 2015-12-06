"""
Codeforces Educational Round 2

Problem 600 E. Lomsat gelral

@author yamaton
@date 2015-11-30
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(pairs, xs, n):
    pass


# def pp(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(c) for c in input().split()]
    pairs = [tuple(int(c) for c in input().split()) for _ in range(n-1)]
    assert len(xs) == n
    result = solve(pairs, xs, n)
    print(*result)


if __name__ == '__main__':
    main()
