#!/usr/bin/env python3
"""
Codeforces
546 A. Soldier and Bananas

@author yamaton
@date 2015-07-29
"""


def solve(k, n, w):
    return max(0, k * w * (1 + w) // 2 - n)


def main():
    [k, n, w] = [int(i) for i in input().strip().split()]
    result = solve(k, n, w)
    print(result)


if __name__ == '__main__':
    main()
