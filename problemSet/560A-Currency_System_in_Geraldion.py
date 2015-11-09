#!/usr/bin/env python3
"""
Codeforces

Problem A. Currency System in Geraldion
http://codeforces.com/problemset/problem/560/A

@author yamaton
@date 2015-07-28
"""
import sys


def solve(n, xs):
    if 1 in xs:
        return -1
    else:
        return 1


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(s) for s in input().strip().split()]
    result = solve(n, xs)
    print(result)


if __name__ == '__main__':
    main()
