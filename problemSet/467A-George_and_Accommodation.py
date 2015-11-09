#!/usr/bin/env python3
"""
Codeforces
467A A. George and Accommodation
http://codeforces.com/problemset/problem/467/A

@author yamaton
@date 2015-07-28
"""


def solve(pqs):
    return sum(p + 2 <= q for (p, q) in pqs)


def main():
    n = int(input())
    pqs = [tuple(int(i) for i in input().split()) for _ in range(n)]
    result = solve(pqs)
    print(result)


if __name__ == '__main__':
    main()
