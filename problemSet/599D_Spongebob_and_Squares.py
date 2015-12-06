"""
Codeforces Round #332 (Div. 2)

Problem 599 D. Spongebob and Squares

@author yamaton
@date 2015-11-20
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(x):
    def numer(n):
        return (6 * x - n * (n + 1) * (2*n + 1))
    def denom(n):
        return 3 * n * (n + 1)

    result = []
    for n in it.count(1):
        num, den = numer(n), denom(n)
        p = num // den
        if p < 0:
            break
        if p * den == num:
            result.append((n, n + p))
            if p > 0:
                result.append((n + p, n))
    result.sort()
    return result


# def p(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    x = int(input())
    results = solve(x)
    print(len(results))
    for res in results:
        print(*res)


if __name__ == '__main__':
    main()
