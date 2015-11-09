"""
Codeforces Round #325 (Div. 2)

Problem 586 B. Laurenty and Shop

@author yamaton
@date 2015-11-09
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def dist(up_adj, down_adj, i):
    assert len(up_adj) == len(down_adj)
    assert 0 <= i <= len(up_adj)
    return sum(up_adj[:i]) + sum(down_adj[i:])


def solve(up_adj, down_adj, up_down):
    distances = sorted(dist(up_adj, down_adj, i) + ud for i, ud in enumerate(up_down))
    return distances[0] + distances[1]


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    ys = [int(i) for i in input().strip().split()]
    zs = [int(i) for i in input().strip().split()]
    assert len(xs) == len(ys) == n-1
    assert len(zs) == n

    result = solve(xs, ys, zs)
    print(result)


if __name__ == '__main__':
    main()
