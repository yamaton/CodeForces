#!/usr/bin/env python3
"""
Codeforces Round #309 (Div. 2)

Problem 554 B. Ohana Cleans Up

@author yamaton
@date 2015-08-17
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xss):
    """
    dirty ... 0
    clean ... 1
    """
    counter = collections.Counter(xss)
    return max(counter.values())


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xss = [input().strip() for _ in range(n)]
    result = solve(xss)
    print(result)


if __name__ == '__main__':
    main()