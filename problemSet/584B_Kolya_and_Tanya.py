"""
Codeforces Round #324 (Div. 2)

Problem 584 B. Kolya and Tanya

@author yamaton
@date 2015-11-11
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

BIG = 1000000007

def solve(n):
    return (3**(3*n) - (6 + 1)**n) % BIG


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)

def main():
    n = int(input())
    result = solve(n)
    print(result)


if __name__ == '__main__':
    main()
