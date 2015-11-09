#!/usr/bin/env python3
"""
Codeforces
567 C. Geometric Progression

@author yamaton
@date 2015-08-05
"""

# import itertools as it
import functools
import operator
import collections
import sys
from math import factorial


def binomial(n, k):
    if n < k:
        return 0
    else:
        return factorial(n) // factorial(k) // factorial(n - k)

def solve(xs, n, k):
    if k == 1:
        return sum(binomial(v, 3) for v in collections.Counter(xs).values() if v >= 3)

    k2 = k * k
    factors = collections.defaultdict(list)
    for r, x in enumerate(xs):
        if x % k2 == 0:
            d[x // k2].append(r)

    count = 0
     for b, rs in factors.items():
        ps = []
        qs = []
        for i, x in enumerate(xs):
            if x == b:
                ps.append(i)
            elif x == b * k:
                qs.append(i)
        if ps and qs:
            pass
    return count


# def print_stderr(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)

 
def main():
    [n, k] = [int(i) for i in input().strip().split()]
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    result = solve(xs, n, k)
    print(result)


if __name__ == '__main__':
    main()
