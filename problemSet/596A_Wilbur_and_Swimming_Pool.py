"""
Codeforces Round #331 (Div. 2)

Problem 596 A. Wilbur and Swimming Pool

@author yamaton
@date 2015-11-15
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(pairs, n):
    if n <= 1:
        return -1

    xmin = min(x for (x, _) in pairs)
    xmax = max(x for (x, _) in pairs)
    ymin = min(y for (_, y) in pairs)
    ymax = max(y for (_, y) in pairs)
    area = (xmax - xmin) * (ymax - ymin)
    if area > 0:
        return area
    else:
        return -1


# def p(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    pairs = [tuple(int(_c) for _c in input().strip().split()) for _ in range(n)]
    assert len(pairs[0]) == 2

    result = solve(pairs, n)
    print(result)


if __name__ == '__main__':
    main()
