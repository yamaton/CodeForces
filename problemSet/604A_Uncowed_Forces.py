"""
Codeforces Round #334 (Div. 2)

Problem 604 A. Uncowed Forces

@author yamaton
@date 2015-12-01
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(ms, ws, hs, hu):
    pts = [500 * i for i in [1, 2, 3, 4, 5]]
    ans = sum(max(3 * x // 10, (x - m * x // 250) - 50 * w)
              for (x, m, w) in zip(pts, ms, ws))
    ans += 100 * hs - 50 * hu
    return ans


# def pp(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    ms = list(map(int, input().split()))
    ws = list(map(int, input().split()))
    hs, hu = map(int, input().split())
    result = solve(ms, ws, hs, hu)
    print(result)


if __name__ == '__main__':
    main()
