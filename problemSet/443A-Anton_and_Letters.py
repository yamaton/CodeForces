#!/usr/bin/env python3
"""
Codeforces
443 A. Anton and Letters

@author yamaton
@date 2015-07-29
"""
import sys


def solve(xs):
    return len(xs)


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    xs = {x.strip() for x in input().strip('{}').split(',') if x}
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
