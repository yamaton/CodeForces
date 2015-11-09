"""
Codeforces Round #321 (Div. 2)

Problem 580 B. Kefa and Company

@author yamaton
@date 2015-09-22
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

import bisect

def solve(xs, d):
    xs.sort()
    ms, fs = list(zip(*xs))
    n = len(ms)

    fsacc = list(it.accumulate(it.chain((0,), fs)))

    out = []
    for i, money in enumerate(ms):
        k = bisect.bisect_right(ms, money + d - 1)
        # print_stderr('----------')
        # print_stderr('i =', i)
        # print_stderr('k =', k)
        # print_stderr('d =', d)
        # print_stderr('ms=', ms)
        # print_stderr('ms[i] =', ms[i])
        # print_stderr('ms[k-1] =', ms[k-1])
        # print_stderr('fs[i] =', fs[i])
        # print_stderr('fs[k-1] =', fs[k-1])

        # out.append(sum(fs[i:k]))
        out.append(fsacc[k] - fsacc[i])
        if k == n:
            break

    return max(out)


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    # Assume the friendship factors are all positive
    [n, d] = [int(i) for i in input().strip().split()]
    money_friend_pairs = [tuple(int(i) for i in input().strip().split()) for _ in range(n)]
    result = solve(money_friend_pairs, d)
    print(result)


if __name__ == '__main__':
    main()
