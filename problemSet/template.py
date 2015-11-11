"""
Codeforces Round #325 (Div. 2)

Problem 586 A

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
    pass


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)

def main():
    m = int(input())
    [n, k, a] = [int(i) for i in input().strip().split()]
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == m

    result = solve(xs, n, k, a)
    print(result)


if __name__ == '__main__':
    main()
