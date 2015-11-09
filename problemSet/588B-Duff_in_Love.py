"""
Codeforces Round #326 (Div. 2)

Problem 588 B. Duff in Love

@author yamaton
@date 2015-10-25
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def psudo_primes():
    yield 2
    yield 3
    x = 5
    while True:
        yield x
        x += 2
        yield x
        x += 4


def factorinteger(n):
    """
    >>> factorinteger(12)
    {2: 2, 3: 1}
    """
    result = collections.defaultdict(int)
    for p in psudo_primes():
        if p * p > n:
            break        
        while n % p == 0:
            result[p] += 1
            n //= p

    if n > 1:
        result[n] += 1
    return dict(result)


def solve(n):
    "O(N^(1/2)) in the worst case"
    if n == 1:
        return 1
    primes = factorinteger(n).keys()
    return functools.reduce(operator.mul, primes)

def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    result = solve(n)
    print(result)


if __name__ == '__main__':
    main()
