"""
Codeforces Round #329 (Div. 2)

Problem 593 A. 2Char

@author yamaton
@date 2015-11-04
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs):
    counts = [collections.Counter(s) for s in xs if len(set(s)) <= 2]
    all_letters = set(it.chain.from_iterable(counts))
    if len(all_letters) <= 1:
        return sum(sum(d.values()) for d in counts)

    maxval = 0
    for (a, b) in it.combinations(all_letters, 2):
        maxlocal = sum(d[a] + d[b] for d in counts if all(l in (a, b) for l in d))
        maxval = max(maxval, maxlocal)
    return maxval


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [input().strip() for _ in range(n)]
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
