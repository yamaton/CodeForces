"""
Codeforces Practice

Problem 1076 C. Meme Problem

@author yamaton
@date 2018-11-27 (Tue)
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

def is_complex(d):
    return d**2 < 4 * d

def formula(d):
    a = (d + math.sqrt(d**2 - 4 * d)) / 2
    b = (d - math.sqrt(d**2 - 4 * d)) / 2
    return a, b

def solve(d):
    if is_complex(d):
        return "N"
    a, b = formula(d)
    if b < 0:
        return "N"
    return f"Y {a} {b}"


def main():
    n = int(input())
    xs = [int(input()) for _ in range(n)]
    for x in xs:
        result = solve(x)
        print(result)


if __name__ == '__main__':
    main()
