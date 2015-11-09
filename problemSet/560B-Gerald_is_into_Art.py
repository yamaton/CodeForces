#!/usr/bin/env python3
"""
Codeforces
560 B. Gerald is into Art
http://codeforces.com/problemset/problem/560/B

@author yamaton
@date 2015-07-28
"""
import sys


def perm(x, y):
    yield (x, y)
    yield (y, x)


def tf_to_yn(tf):
    return 'YES' if tf else 'NO'


def solve(a1, b1, a2, b2, a3, b3):
    for side1, rem1 in perm(a1, b1):
        for side2, rem2 in perm(a2, b2):
            for side3, rem3 in perm(a3, b3):
                if (side1 >= side2 + side3 and rem1 >= rem2 and rem1 >= rem3):
                    return True
    return False


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    xs = [int(s) for _ in range(3) for s in input().strip().split()]
    result = tf_to_yn(solve(*xs))
    print(result)


if __name__ == '__main__':
    main()
