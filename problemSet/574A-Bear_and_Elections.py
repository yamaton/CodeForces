#!/usr/bin/env python3
"""
Codeforces Round #318 (Div. 2)

Problem A. Bear and Elections

@author yamaton
@date 2015-08-31
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs):
    points = points0 = xs[0]
    bribes = 0
    others = sorted(xs[1:], reverse=True)

    for x in others:
        if x >= points:
            diff = x - points
            points += diff // 2 + 1
    return points - points0


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n

    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
