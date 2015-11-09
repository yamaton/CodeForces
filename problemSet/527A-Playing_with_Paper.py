#!/usr/bin/env python3
"""
Codeforces
527 A. Playing with Paper

@author yamaton
@date 2015-08-04
"""


def solve(a, b):
    cnt = 0
    while b > 0:
        cnt += a // b        
        a, b = b, a % b
    return cnt


def main():
    [a, b] = [int(i) for i in input().strip().split()]
    result = solve(a, b)
    print(result)


if __name__ == '__main__':
    main()
