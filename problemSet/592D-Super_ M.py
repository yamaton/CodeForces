"""
Codeforces Round #328 (Div. 2)

Problem 592 D. Super Ms

@author yamaton
@date 2015-10-31
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(edges, attacked_nodes):
    pass


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    pairs =  [[int(i) for i in input().strip().split()] for _ in range(n-1)]
    attacked = [int(i) for i in input().strip().split()]
    assert len(attacked) == m
    city, time = solve(pairs, attacked)
    print(city)
    print(time)


if __name__ == '__main__':
    main()
