"""
Codeforces Round #126 (Div. 2)

Problem 200 B. Drinks

@author yamaton
@date 2015-11-08
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def chunks(iterable, n, fillvalue=None):
    """
    modified grouper function
    https://docs.python.org/3.5/library/itertools.html

    >>> list(chunks([1, 2, 3, 4, 5, 6, 7], 3))
    [(1, 2, 3), (4, 5, 6)]
    """
    args = [iter(iterable)] * n
    return zip(*args)


def solve(xs, ys):
    zs = xs + ys




def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n

    result = solve(xs, n)
    print(result)


if __name__ == '__main__':
    main()
