"""
Codeforces Educational Round 2

Problem 600 B. Queries about less or equal elements

@author yamaton
@date 2015-11-30
"""

import bisect


def solve(xs, ys):
    xs.sort()
    return [bisect.bisect_right(xs, y) for y in ys]


def main():
    n, m = map(int, input().split())
    xs = [int(c) for c in input().split()]
    ys = [int(c) for c in input().split()]
    assert len(xs) == n
    assert len(ys) == m
    result = solve(xs, ys)
    print(*result)


if __name__ == '__main__':
    main()
