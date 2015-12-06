"""
Codeforces Round #324 (Div. 2)

Problem 584 A Olesya and Rodion

@author yamaton
@date 2015-11-11
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(n, t):
    count = (10**n - 1) // t -  (10**(n-1) - 1) // t
    if count == 0:
        return -1
    else:
        return (10**n -1) // t * t


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)

def main():
    [n, t] = [int(c) for c in input().strip().split()]
    result = solve(n, t)
    print(result)


if __name__ == '__main__':
    main()
