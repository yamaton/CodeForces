#!/usr/bin/env python3
"""
Codeforces
270 A. Fancy Fence

@author yamaton
@date 2015-08-04
"""


def solve(x):
    return 360 % (180 - x) == 0


def tf_to_yn(tf):
    return 'YES' if tf else 'NO'


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        result = solve(x)
        print(tf_to_yn(result))


if __name__ == '__main__':
    main()
