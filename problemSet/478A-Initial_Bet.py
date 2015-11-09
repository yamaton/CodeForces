#!/usr/bin/env python3
"""
Codeforces
478 A. Initial Bet

@author yamaton
@date 2015-07-29
"""
import sys


def solve(xs):
    total = sum(xs)
    if total % 5 > 0 or total == 0:
        return -1
    else:
        return total // 5


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    cs = [int(i) for i in input().strip().split()]
    assert len(cs) == 5
    result = solve(cs)
    print(result)


if __name__ == '__main__':
    main()
