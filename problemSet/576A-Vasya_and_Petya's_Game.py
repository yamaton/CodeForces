#!/usr/bin/env python3
"""
Codeforces Round #319 (Div. 2)

Problem 576 A. / 577 C. Vasya and Petya's Game

@author yamaton
@date 2015-09-10
"""

import itertools as it
import functools
import operator
import collections
import math
import sys



def EratosthenesSieve(N):
    """Construct a list of primes equal or less than N.

    >>> EratosthenesSieve(8)
    [2, 3, 5, 7]
    """
    numbers = [True] * (N + 1)
    max_p = int(math.sqrt(N))
    for p in (i for i in range(2, max_p + 1) if numbers[i]):
        for q in range(p * p, N + 1, p):
            numbers[q] = False
    return [i for i in range(2, N + 1) if numbers[i]]


def solve(n):
    ys = []
    for i in EratosthenesSieve(n):
        ys.append(i)        
        current = i*i
        while current <= n:
            ys.append(current)
            current *= i
    return ys


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    ys = solve(n)
    print(len(ys))
    print(' '.join(str(i) for i in ys))


if __name__ == '__main__':
    main()
