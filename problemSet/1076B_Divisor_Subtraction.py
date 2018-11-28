"""
Codeforces Practice

Problem 1076 B. Divisor Subtraction

@author yamaton
@date 2018-11-27 (Tue)
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def pseudo_prime():
    yield 3
    yield 5
    yield 7
    i = 11
    while True:
        yield i
        yield i + 2
        i += 4


def solve(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return n // 2

    pseudo_primes = it.takewhile(lambda k: k < int(n**0.5 + 1), pseudo_prime())
    for d in pseudo_primes:
        if n % d == 0:
            res = d
            break
    else:
        res = n
    return 1 + solve(n - res)


def main():
    n = int(input())
    result = solve(n)
    print(result)


if __name__ == "__main__":
    main()
