#!/usr/bin/env python3
"""
Codeforces
492 A. Vanya and Cubes

@author yamaton
@date 2015-07-29
"""
import itertools


def solve(n):
    def f(x):
        return x * (x + 1) * (x + 2) // 6

    out = itertools.takewhile(lambda i: i <= n, map(f, itertools.count(1)))
    return sum(1 for _ in out)


def test():
    assert solve(1) == 1
    assert solve(25) == 4


def main():
    n = int(input())
    result = solve(n)
    print(result)


if __name__ == '__main__':
    main()
