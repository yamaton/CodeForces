"""
Codeforces Round #322 (Div. 2)

Problem 581 A. Vasya the Hipster

@author yamaton
@date 2015-10-06
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(a, b):
    return min(a, b), abs(a - b) // 2


def main():
    [a, b] = [int(i) for i in input().strip().split()]
    red, blue = solve(a, b)
    print(red, blue)


if __name__ == '__main__':
    main()
