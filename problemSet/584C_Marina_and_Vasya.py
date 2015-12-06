"""
Codeforces Round #324 (Div. 2)

Problem 584 C Marina and Vasya

@author yamaton
@date 2015-11-11
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(s1, s2, n, t):
    mismatches = sum(c1 != c2 for (c1, c2) in zip(s1, s2))
    matches = n - mismatches

    if t < (mismatches + 1) // 2:
        return -1

    if t <= mismatches:
        rest = t - (mismatches + 1) // 2


    return ''.join(result)


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)

def main():
    [n, t] = [int(c) for c in input().strip().split()]
    s1 = input().strip()
    s2 = input().strip()
    assert len(s1) == len(s2) == n
    result = solve(s1, s2, n, t)
    print(result)


if __name__ == '__main__':
    main()
