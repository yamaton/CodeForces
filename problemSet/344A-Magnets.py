#!/usr/bin/env python3
"""
Codeforces
344 A. Magnets

@author yamaton
@date 2015-07-28
"""
import sys
import itertools


def solve(xs):
    return sum(1 for _ in itertools.groupby(xs))


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [input().strip() for _ in range(n)]
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
