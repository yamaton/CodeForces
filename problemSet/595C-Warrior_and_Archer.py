"""
Codeforces Round #330 (Div. 2)

Problem 595 C. Warrior and Archer

@author yamaton
@date 2015-11-08
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

sys.setrecursionlimit(10000000)


@functools.lru_cache(None)
def distance(xs, player):
    if len(xs) > 2:
        return distance(move(xs, player), 1 - player)
    else:
        (a, b) = xs
        return abs(b - a)


@functools.lru_cache(None)
def move(xs, player):
    n = len(xs)
    candidates = [tuple(xs[:i] + xs[i+1:]) for i in range(n)]
    if player == 0:
        return min(candidates, key=lambda ys: distance(ys, 1 - player))
    else:
        return max(candidates, key=lambda ys: distance(ys, 1 - player))


def solve(xs):
    xs = tuple(sorted(xs))
    return distance(xs, 0)


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n

    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
