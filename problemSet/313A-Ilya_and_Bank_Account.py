#!/usr/bin/env python3
"""
Codeforces
313 A. Ilya and Bank Account

@author yamaton
@date 2015-08-03
"""
import itertools

def solve(n):
    if n >= 0:
        return n
    else:
        s = str(n)
        xs = list(s)
        a = int(''.join(xs[:-1]))
        b = int(''.join(xs[:-2] + [xs[-1]]))
        return max(a, b)


def main():
    n = int(input())
    result = solve(n)
    print(result)


if __name__ == '__main__':
    main()
