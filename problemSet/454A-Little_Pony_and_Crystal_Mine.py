#!/usr/bin/env python3
"""
Codeforces
454 A. Little Pony and Crystal Mine

@author yamaton
@date 2015-08-04
"""


def solve(n):
    k = (n + 1) // 2
    xs = [2*i + 1 for i in range(k)] 
    ys = ['D' * n for n in (xs + xs[::-1][1:])]
    return [s.center(n, '*') for s in ys]


def main():
    n = int(input())
    result = solve(n)
    for line in result:
        print(line)


if __name__ == '__main__':
    main()
