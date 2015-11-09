"""
Codeforces Round #328 (Div. 2)

Problem 592 C. The Big Race

@author yamaton
@date 2015-10-31
"""

import itertools as it
import functools
import operator
import collections
import math
import sys
import fractions


def lcm(a, b):
    return a * b // fractions.gcd(a, b)

def solve(t, w, b):
    k = min(w, b)
    interval = lcm(w, b)
    cycles, reminder = divmod(t, interval)
    result = cycles * k + min(k - 1, reminder)
    g = fractions.gcd(result, t)
    return "%d/%d" % (result // g, t // g)

def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [t, w, b] = [int(i) for i in input().strip().split()]
    result = solve(t, w, b)
    print(result)


if __name__ == '__main__':
    main()
