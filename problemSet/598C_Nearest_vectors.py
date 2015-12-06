"""
Codeforces Educational Round

Problem 598 C. Nearest vectors

@author yamaton
@date 2015-11-12
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(pairs, n):
    angles_indices = sorted((math.atan2(y, x), i) for (i, (x, y)) in enumerate(pairs))

    result = (0, 0)
    min_angle = 10000
    for i in range(n):
        ang = angles_indices[(i+1) % n][0] - angles_indices[i][0]
        if ang < 0:
            ang += 2 * math.pi
        if ang < min_angle:
            result = (angles_indices[i][1] + 1, angles_indices[(i + 1) % n][1] + 1)
            min_angle = ang

    return result


def main():
    n = int(input())
    pairs = [tuple(int(c) for c in input().strip().split()) for _ in range(n)]
    (a, b) = solve(pairs, n)
    print(str(a) + ' ' + str(b))


if __name__ == '__main__':
    main()
