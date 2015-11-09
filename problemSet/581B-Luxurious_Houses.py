"""
Codeforces Round #322 (Div. 2)

Problem 581 B. Luxurious Houses

@author yamaton
@date 2015-10-06
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs):
    max_height = 0
    result = []
    for x in reversed(xs):
        if x > max_height:
            result.append(0)
            max_height = x
        else:
            additional = max_height - x + 1
            result.append(additional)
    return reversed(result)


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n

    result = solve(xs)
    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
