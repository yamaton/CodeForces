"""
Codeforces Round #329 (Div. 2)

Problem 593 B. Anton and Lines

@author yamaton
@date 2015-11-04
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def intersects(x1, x2, line1, line2):
    (k1, b1) = line1
    (k2, b2) = line2
    at_x1 = (k2 - k1) * x1 + (b2 - b1)
    at_x2 = (k2 - k1) * x2 + (b2 - b1)
    return at_x1 * at_x2 < 0

def solve(x1, x2, kbs):
    at_x1 = [k*x1 + b for (k, b) in kbs]
    at_x2 = [k*x2 + b for (k, b) in kbs]
    order1 = [i for i, _ in sorted(enumerate(at_x1), key=operator.itemgetter(1))]
    order2 = [i for i, _ in sorted(enumerate(at_x2), key=operator.itemgetter(1))]
    return order1 == order2


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def tf_to_yn(tf):
    return 'YES' if tf else 'NO'


def main():
    n = int(input())
    [x1, x2] = [int(i) for i in input().strip().split()]
    kbs = [tuple(int(i) for i in input().strip().split()) for _ in range(n)]
    result = solve(x1, x2, kbs)
    print(tf_to_yn(result))


if __name__ == '__main__':
    main()
