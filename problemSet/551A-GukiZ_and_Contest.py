#!/usr/bin/env python3
"""
Codeforces
551 A. GukiZ and Contest

@author yamaton
@date 2015-08-04
"""


def solve(xs):
    return [sum(1 for y in xs if y > x) + 1 for x in xs]


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    result = solve(xs)
    print(' '.join(str(n) for n in result))


if __name__ == '__main__':
    main()
