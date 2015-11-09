#!/usr/bin/env python3
"""
Codeforces Round #309 (Div. 1/2)

Problem 553B / 554D. Kyoya and Colored Balls

@author yamaton
@date 2015-08-17
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(n, k):
    pass


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, k] = [int(input()) for _ in range(n)]
    result = solve(n, k)
    print(' '.join(str(n) for n in result))

if __name__ == '__main__':
    main()