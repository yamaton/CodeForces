#!/usr/bin/env python3
"""
Codeforces
461 A. Appleman and Toastman

@author yamaton
@date 2015-08-04
"""


def solve(xs):
    xs.sort()
    return sum(i * x for (i, x) in enumerate(xs, 2)) - xs[-1]


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
