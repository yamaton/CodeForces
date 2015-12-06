"""
Codeforces Testing Round #12

Problem 597C. Subsequences

@author yamaton
@date 2015-11-11
"""

import math
import operator
import random
import sys

import functools


def binomial(n: int, k: int) -> int:
    """
    >>> binomial(4, 0)
    1
    >>> binomial(4, 1)
    4
    >>> binomial(4, 2)
    6
    >>> binomial(4, 3)
    4
    >>> binomial(4, 4)
    1

    See `sympy.binomial` and `scipy.special.binom` for better implementations
    """
    if n < k:
        return 0
    elif n < 2 * k:
        return binomial(n, n - k)
    else:
        numer = functools.reduce(operator.mul, range(n, n - k, -1), 1)
        denom = functools.reduce(operator.mul, range(k, 0, -1), 1)
        return numer // denom


def solve(xs, n, k):
    """
    Number of increasing subsequences with (k+1) length
    :param xs: List[int]
    :param k:  int
    :return:   int
    """
    d = dict()  # {last_element: length}
    for
    for i, x in enumerate(xs):
        update = [(x, length + 1) if last_elem < x else (last_elem, length)
                  for (last_elem, length) in lis]
        if update:
            lis = update
        else:
            lis.append((x, 1))

    return sum(binomial(l, k) for _, l in lis if k <= l)


def p(*args, **kwargs):
    return print(file=sys.stderr, *args, **kwargs)


def main():
    [n, k] = [int(i) for i in input().strip().split()]
    xs = [int(input()) for _ in range(n)]
    result = solve(xs, n, k)
    print(result)


if __name__ == '__main__':
    main()
