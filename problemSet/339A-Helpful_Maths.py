#!/usr/bin/env python3
"""
Codeforces
339 A. Helpful Maths
http://codeforces.com/problemset/problem/339/A

@author yamaton
@date 2015-07-28
"""
import sys


def solve(s):
    xs = s.split('+')
    xs.sort()
    return '+'.join(xs)


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    xs = input().strip()
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
