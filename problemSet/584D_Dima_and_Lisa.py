"""
Codeforces Round #324 (Div. 2)

Problem 584 D Dima and Lisa

@author yamaton
@date 2015-11-11
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


@functools.lru_cache(maxsize=None)
def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    max_p = int(math.sqrt(n))
    return all(n % p != 0 for p in range(3, max_p + 1, 2))


def sieve(n):
    m = (n + 1) // 2
    remaining = [True] * m
    max_p = int(math.sqrt(n))
    for p in range(3, max_p + 1, 2):
        if not remaining[p]:
            continue
        for q in range(p * p, n + 1, p):
            remaining[q] = False
    return [p for p in range(2, n + 1) if remaining[p]]


def solve(n):
    cnt = 0
    if isprime(n):
        cnt += 1
    if isprime(n-2):
        cnt += 1
    if isprime(n-4):
        cnt += 1
    else:
        for i in range(3, n // 3, 2):
            if not isprime(i):
                continue
            for j in (i, n //3, 2):
                if not isprime(j):
                    continue
                if isprime(n - i - j):
                    return [i, j, n - i - j]


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)

def main():
    n = int(input())
    k, ps = solve(n)
    print(k)
    print(' '.join(str(p) for p in ps))

if __name__ == '__main__':
    main()
