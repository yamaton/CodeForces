"""
Codeforces Round #332

Problem 599 C. Day at the Beach

@author yamaton
@date 2015-11-20
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

# concise answer
def solve(xs, n):
    max_upto = list(it.accumulate(xs, max))
    min_after = list(it.accumulate(reversed(xs), min))
    min_after.reverse()
    cnt = 1 + sum(1 for (left_max, right_min) in zip(max_upto, min_after[1:])
                    if left_max <= right_min)
    return cnt


def solve_submitted(xs, n):
    max_upto = []
    maxval = 0
    for x in xs:
        maxval = max(maxval, x)
        max_upto.append(maxval)

    min_after = []
    minval = 10000000000
    for x in reversed(xs):
        minval = min(minval, x)
        min_after.append(minval)
    min_after.reverse()

    cnt = 1
    for i in range(1, n):
        if max_upto[i-1] <= min_after[i]:
            cnt += 1

    return cnt



@functools.lru_cache(maxsize=None)
def count(tup):
    if len(tup) == 1:
        return 1

    maxval = 1
    n = len(tup)
    for i in range(1, n):
        first = tup[:i]
        second = tup[i:]
        if max(first) <= min(second):
            maxval = max(maxval, count(first) + count(second))
    return maxval

# A bruteforce approach
def solve_bruteforce(xs, n):
    return count(tuple(xs))


# def p(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(_c) for _c in input().strip().split()]

    result = solve(xs, n)
    print(result)


if __name__ == '__main__':
    main()
