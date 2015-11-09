"""
Codeforces Round #322 (Div. 2)

Problem 581 C. Developing Skills

@author yamaton
@date 2015-10-06
"""

import itertools as it
import functools
import operator
import collections
import math
import sys
import bisect


# def solve_fp(xs, k):
#     n = len(xs)
#     current_level = sum(x // 10 for x in xs)
#     remaining_points = sorted([(100 - x) % 10 for x in xs
#                                if x < 100 and x % 10 > 0])
#     inf_series = it.accumulate(it.chain(remaining_points, it.repeat(10)))
#     acc_points = list(it.takewhile(lambda total: sum(xs) + total <= 100 * n, inf_series))
#     levelups = bisect.bisect_right(acc_points, k)
#     return current_level + levelups


def solve(xs, k):
    n = len(xs)
    max_possible = 10 * n
    current_level = sum(x // 10 for x in xs)
    remaining_points = sorted([(100 - x) % 10
                               for x in xs
                               if x < 100 and x % 10 > 0])
    acc_points = list(it.accumulate(remaining_points))
    m = len(acc_points)  # number of skills for possible levelups
    levelups = bisect.bisect_right(acc_points, k)

    if m == 0:
        return min(max_possible, current_level + k // 10)
    elif levelups < m:
        return min(max_possible, current_level + levelups)
    else:
        rest = k - acc_points[-1]
        return min(max_possible, current_level + levelups + rest // 10)


def main():
    [n, k] = [int(i) for i in input().strip().split()]
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n

    result = solve(xs, k)
    print(result)


if __name__ == '__main__':
    main()
