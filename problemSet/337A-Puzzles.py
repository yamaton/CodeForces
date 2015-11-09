#!/usr/bin/env python3
"""
Codeforces
337 A. Puzzles

@author yamaton
@date 2015-07-29
"""
import sys


def solve(xs, n, m):
    xs.sort()
    return min(xs[i + n - 1] - xs[i] for i in range(m - n + 1))


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    fs = [int(i) for i in input().strip().split()]
    assert len(fs) == m
    # print_stderr(fs, n, m)
    result = solve(fs, n, m)
    print(result)


if __name__ == '__main__':
    main()
