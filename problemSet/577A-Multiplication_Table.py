#!/usr/bin/env python3
"""
Codeforces Round #319 (Div. 2)

Problem 577 A. Multiplication Table

@author yamaton
@date 2015-09-10
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(n, x):
    sqrtx = int(math.sqrt(x))
    lim = min(sqrtx, n)
    count = sum(2 for d in range(1, lim + 1) if x % d == 0 and x <= n * d)
    if sqrtx **2 == x and sqrtx <= n:
        count -= 1
    return count


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, x] = [int(i) for i in input().strip().split()]
    result = solve(n, x)
    print(result)


if __name__ == '__main__':
    main()
