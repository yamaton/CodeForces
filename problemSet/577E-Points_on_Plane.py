#!/usr/bin/env python3
"""
Codeforces Round #319 (Div. 2)

Problem 577 E. Points on Plane

@author yamaton
@date 2015-09-10
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def dist(p, q):
    return sum(abs(pi - qi) for (pi, qi) in zip(p, q))


## split grid into 1000 x 1000 regions
## or region with length 10^6 // 1000 = 1000
def solve(points):
    SIZE = 1000
    points.sort()

    regions = collections.defaultdict(list)
    for idx, (x, y) in enumerate(points):
        address_x = min(x // SIZE, 999)
        address_y = min(y // SIZE, 999)
        coord = (address_x, address_y)
        regions[coord].append(idx)

    for j in range(100):
        if j % 2 == 0:
            for i in range(1000):
                yield regions[(i, j)]
        else:
            for i in reversed(range(1000)):
                yield reversed(regions[(i, j)])


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    points = [tuple(int(i) for i in input().strip().split()) for _ in range(n)]

    result = list(solve(points))
    d = list(enumerate(points, 1))
    print(sum(dist(d[idx1], d[idx2]) for (idx1, idx2) in zip(result, result[1:])))
    # print(' '.join(str(i) for i in it.chain.from_iterable(resultt)))


if __name__ == '__main__':
    main()
