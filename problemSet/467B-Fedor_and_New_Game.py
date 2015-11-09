"""
Codeforces Round #267 (Div. 2)

Problem 467 B. Fedor and New Game

@author yamaton
@date 2015-09-22
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs, n, m, k):
    def diff(a, b):
        return sum(1 for (ca, cb) in zip(a, b) if ca != cb)

    ys = [bin(x)[2:].zfill(n) for x in xs]
    fedor = ys[-1]
    rest = ys[:-1]
    return sum(1 for x in rest if diff(x, fedor) <= k) 


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, m, k] = [int(i) for i in input().strip().split()]
    xs = [int(input().strip()) for _ in range(m+1)]
    result = solve(xs, n, m, k)
    print(result)


if __name__ == '__main__':
    main()
