"""
Codeforces Round #310 (Div. 2)

Problem 556 A. Case of the Zeros and Ones

@author yamaton
@date 2015-09-22
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs):
    n = len(xs)
    zeros = sum(1 for x in xs if x == 0)
    ones = n - zeros
    return abs(zeros - ones)


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(i) for i in input().strip()]
    assert len(xs) == n

    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
