"""
Codeforces Educational Round

Problem 598 C

@author yamaton
@date 2015-11-12
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs):
    pass


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)

def main():
    n = int(input())
    [a, b, k] = [int(c) for c in input().strip().split()]
    mat = [[int(c) for c in input().strip().split()] for _ in range(n)]
    assert len(xs) == n

    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
