"""
Codeforces Practice

Problem 1076 A. Minimizing the String

@author yamaton
@date 2018-11-27
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(s):
    idx = len(s) - 1
    for i, (c1, c2) in enumerate(zip(s, s[1:])):
        if c1 > c2:
            idx = i
            break
    return s[:idx] + s[idx + 1 :]


def main():
    n = int(input())
    s = input().strip()
    assert len(s) == n
    result = solve(s)
    print(result)


if __name__ == "__main__":
    main()
