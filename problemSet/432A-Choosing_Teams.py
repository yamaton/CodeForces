#!/usr/bin/env python3
"""
Codeforces
432 A. Choosing Teams

@author yamaton
@date 2015-08-04
"""


def solve(ys, k):
    return sum(1 for y in ys if y + k <= 5) // 3


def main():
    [n, k] = [int(i) for i in input().strip().split()]
    ys = [int(i) for i in input().strip().split()]
    assert len(ys) == n
    result = solve(ys, k)
    print(result)


if __name__ == '__main__':
    main()
