"""
Codeforces Round 332 (Div. 2)

Problem 599 E. Sandy and Nuts

@author yamaton
@date 2015-11-20
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(pairs, triples, n, m, q):
    pass


# def p(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    [n, m, q] = map(int, input().strip().split())
    xs = [int(c) for c in input().strip().split()]
    pairs = [tuple(int(c) for c in input().strip().split()) for _ in range(m)]
    triples = [[int(c) for c in input().strip().split()] for _ in range(q)]
    result = solve(pairs, triples, n, m, q)
    print(result)


if __name__ == '__main__':
    main()
