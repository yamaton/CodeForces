"""
Codeforces Round #334 (Div. 2)

Problem 604 D. Moodular Arithmetic

@author yamaton
@date 2015-12-01
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(p, k):
    k %= p



# def pp(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    p, k = map(int, input().split())
    result = solve(p, k)
    print(result)


if __name__ == '__main__':
    main()
