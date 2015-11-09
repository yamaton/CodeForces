"""
Codeforces Round #325 (Div. 2)

Problem 586 A. Alena's Schedule

@author yamaton
@date 2015-11-09
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs):
    ys = it.dropwhile(lambda x: x == 0, (reversed(list(it.dropwhile(lambda x: x == 0, reversed(xs))))))
    zs = [(x, sum(1 for _ in iterable)) for x, iterable in it.groupby(ys)]
    print('zs =', zs, file=sys.stderr)
    return sum(cnt for (x, cnt) in zs if not (x == 0 and cnt > 1))


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n

    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
