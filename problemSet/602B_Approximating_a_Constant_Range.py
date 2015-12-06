"""
Codeforces Round 333 (Div. 2)

Problem 602 B. Approximating a Constant Range

@author yamaton
@date 2015-11-24
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs, n):
    max_upto = [[0] * n for _ in range(n)]
    min_upto =
    for i in range(n):
        for j in range(i+1, n):
            max_upto[i][j] = max(xs[j], max_upto[i][j-1])
            min_upto[i][j] = min(xs[j], min_upto[i][j-1])

    max_after = [xs[-1]] * n
    min_after = [xs[-1]] * n
    for i in range(n-2, -1, -1):
        max_after[i] = max(xs[i], max_after[i+1])
        min_after[i] = min(xs[i], min_after[i+1])

    return max(j - i + 1 for i in range(n) for j in range(i, n)
               if max(max_after[i], max_upto[j]) - min(min_after[i], min_upto[j]) < 2)

#
# def solve(xs, n):
#     maxlength = 1
#     local = 1
#     min_so_far = xs[0]
#     max_so_far = xs[0]
#     for x in xs[1:]:
#         if max(x, max_so_far) - min(x, min_so_far) <= 1:
#             local += 1
#             maxlength = max(maxlength, local)
#             max_so_far = max(x, max_so_far)
#             min_so_far = min(x, min_so_far)
#         else:
#             local = 1
#             min_so_far = x
#             max_so_far = x
#         pp('max_so_far', max_so_far)
#         pp('min_so_far', min_so_far)
#         pp('x', x)
#         pp('(maxlen, local) = ', (maxlength, local))
#     return maxlength
#

def pp(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(c) for c in input().strip().split()]
    assert len(xs) == n
    result = solve(xs, n)
    print(result)


if __name__ == '__main__':
    main()
