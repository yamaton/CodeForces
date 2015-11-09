"""
Codeforces Round #329 (Div. 2)

Problem 593 C. Beautiful Function

@author yamaton
@date 2015-11-04
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(triples):
    pass


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    triples = [tuple(int(i) for i in input().strip().split()) for _ in range(n)]
    result = solve(triples)
    # print(result)


if __name__ == '__main__':
    main()
