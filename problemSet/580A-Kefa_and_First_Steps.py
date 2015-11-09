"""
Codeforces Round #321 (Div. 2)

Problem 580 A. Kefa and First Steps

@author yamaton
@date 2015-09-22
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs):
    cnt = {0: 0}
    prev = 0

    for i, x in enumerate(xs, 1):
        if prev <= x:
            cnt[i] = cnt[i-1] + 1
        else:
            cnt[i] = 1
        prev = x

    return max(cnt.values())


def solve2(xs):
    neighbors = zip(xs, xs[1:])
    acc = 1

    maxval = 0
    for (a, b) in neighbors:
        if a <= b:
            acc += 1
        else:
            acc = 1
        maxval = max(maxval, acc)

    return maxval


def scanl(f, ini, iterable):
    """
    Return list of fold operation
    (inspired by scanl in Haskell) 
    scanl(f, x, [p0, p1, p2]) 
    -> iterator of [x, f(x, p1), f(f(x, p0), p1), f(f(f(x, p0), p1), p2)]

    >>> import operator
    >>> tmp = scanl(operator.add, 5, [1, 2, 3])
    >>> list(tmp)
    [5, 6, 8, 11]
    """
    return it.accumulate(it.chain((ini,), iterable), f)


def solve3(xs):
    def _f(acc, pair):
        a, b = pair
        if a <= b:
            return acc + 1
        else:
            return 1    
    neighbors = zip(xs, xs[1:])
    iterable = scanl(_f, 1, neighbors)
    return max(iterable)


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n

    result = solve3(xs)
    print(result)


if __name__ == '__main__':
    main()
