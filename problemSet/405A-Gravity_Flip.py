#!/usr/bin/env python3
"""
Codeforces
405 A. Gravity Flip

@author yamaton
@date 2015-08-02
"""


def solve(xs):
    return ' '.join(str(i) for i in sorted(xs))


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert n == len(xs)
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
