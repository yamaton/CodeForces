#!/usr/bin/env python3
"""
Codeforces
459 B. Pashmak and Flowers

@author yamaton
@date 2015-08-05
"""


def solve(xs):
    xs.sort()
    ll = len(xs)
    max_diff = xs[-1] - xs[0]
    if max_diff == 0:
        count = ll * (ll - 1) // 2
    else:
        count = xs.count(xs[0]) * xs.count(xs[-1])
    return max_diff, count


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    result = solve(xs)
    print(' '.join(str(n) for n in result))


if __name__ == '__main__':
    main()
