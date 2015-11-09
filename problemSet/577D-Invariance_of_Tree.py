#!/usr/bin/env python3
"""
Codeforces Round #319 (Div. 2)

Problem 577 D. Invariance of Tree

@author yamaton
@date 2015-09-10
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs):
    pass


def tf_to_yn(tf):
    return 'YES' if tf else 'NO'


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == m

    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
