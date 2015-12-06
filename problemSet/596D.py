"""
Codeforces Round #331 (Div. 2)

Problem 596 C

@author yamaton
@date 2015-11-15
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs):
    pass


# def p(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    [a, b, c] = map(int, input().strip().split())
    xs = [int(_c) for _c in input().strip().split()]
    xss = [[int(_c) for _c in input().strip().split()] for _ in range(n)]

    result = solve(xs, n)
    print(result)


if __name__ == '__main__':
    main()
