#!/usr/bin/env python3
"""
Codeforces Round #309 (Div. 1/2)

Problem 553 A. Kyoya and Colored Balls

@author yamaton
@date 2015-08-17
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


LARGE_NUMBER = 1000000007

@functools.lru_cache(maxsize=None)
def binomial(n, k):
    """
    >>> binomial(4, 0)
    1
    >>> binomial(4, 1)
    4
    >>> binomial(4, 2)
    6
    >>> binomial(4, 3)
    4
    >>> binomial(4, 4)
    1
    """
    if n < k:
        return 0
    elif n < 2 * k:
        return binomial(n, n - k)
    else:
        numer = functools.reduce(operator.mul, range(n, n - k, -1), 1)
        denom = functools.reduce(operator.mul, range(k, 0, -1), 1)
        return numer // denom


def solve(xs):
    n = len(xs)
    for i in range(n):
        if i == 0:
            count = 1
        count *= binomial(sum(xs[:i+1]) - 1, xs[i] - 1) 
        count %= LARGE_NUMBER
    return count


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(input()) for _ in range(n)]
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()