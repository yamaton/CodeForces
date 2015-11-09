#!/usr/bin/env python3
"""
Codeforces Round #317 (Div. 2)

Problem 572 B. Order Book

@author yamaton
@date 2015-08-23
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xss, s):
    order = collections.defaultdict(int)
    for (d, p, q) in xss:
        order[(d, int(p))] += int(q)

    sells = sorted([(d, p, q) for ((d, p), q) in order.items() if d == 'S'], reverse=True)
    buys =  sorted([(d, p, q) for ((d, p), q) in order.items() if d == 'B'], reverse=True)
    return sells[-s:] + buys[:s]


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, s] = [int(i) for i in input().strip().split()]
    xss = [input().strip().split() for _ in range(n)]
    result = solve(xss, s)
    for line in result:
        print(' '.join(str(n) for n in line))


if __name__ == '__main__':
    main()
