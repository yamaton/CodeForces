#!/usr/bin/env python3
"""
Codeforces
451 A. Game with Sticks

@author yamaton
@date 2015-07-28
"""


def solve(n, m):
    if min(n, m) % 2 == 0:
        return 'Malvika'
    else:
        return 'Akshat'


def test():
    assert solve(2, 2) == 'Malvika'
    assert solve(2, 3) == 'Malvika'
    assert solve(3, 3) == 'Akshat'


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    result = solve(n, m)
    print(result)


if __name__ == '__main__':
    main()
