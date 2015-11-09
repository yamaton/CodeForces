"""
Codeforces Round #330 (Div. 2)

Problem 595 A. Vitaly and Night

@author yamaton
@date 2015-11-08
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

def chunks(iterable, n):
    """
    modified grouper function
    https://docs.python.org/3.5/library/itertools.html

    >>> list(chunks([1, 2, 3, 4, 5, 6, 7], 3))
    [(1, 2, 3), (4, 5, 6)]
    """
    args = [iter(iterable)] * n
    return zip(*args)


def solve(xss):
    xs = it.chain.from_iterable(xss)
    return sum(a + b >= 1 for (a, b) in chunks(xs, 2))


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    xss = [[int(i) for i in input().strip().split()] for _ in range(n)]
    assert len(xss[0]) == 2*m
    result = solve(xss)
    print(result)


if __name__ == '__main__':
    main()
