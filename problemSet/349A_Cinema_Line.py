"""
Codeforces Round 

Problem 349 A. Cinema Line

@author yamaton
@date 2015-12-01
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs, n):
    changes = collections.defaultdict(int)
    for x in xs:
        if x == 50:
            changes[25] -= 1
        elif x == 100:
            if changes[50] > 0:
                changes[50] -= 1
                changes[25] -= 1
            else:
                changes[25] -= 3
        changes[x] += 1
        if any(v < 0 for v in changes.values()):
            return 'NO'
    return 'YES'


def main():
    n = int(input())
    xs = [int(c) for c in input().split()]
    assert len(xs) == n
    result = solve(xs, n)
    print(result)


if __name__ == '__main__':
    main()
