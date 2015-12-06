"""
Codeforces Round #332

Problem 599 A. Patrick and Shopping

@author yamaton
@date 2015-11-20
"""

import sys


def solve(d1, d2, d3):
    return min(d1 + d2 + d3, 2*(d1 + d2), 2*(d1 + d3), 2*(d2 + d3))


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def main():
    [d1, d2, d3] = map(int, input().strip().split())
    result = solve(d1, d2, d3)
    print(result)


if __name__ == '__main__':
    main()
