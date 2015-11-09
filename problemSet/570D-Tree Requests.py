#!/usr/bin/env python3
"""
Codeforces Round #316 (Div. 2)

Problem D. Tree Requests

@author yamaton
@date 2015-08-13
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(s, pairs):


def tf_to_yn(tf):
    return 'Yes' if tf else 'No'

def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    ps = [int(i) for i in input().strip().split()]
    assert len(ps) == n - 1

    s = input().strip()

    letter_vertex_pairs = [[int(i) for i in input().strip().split()] for _ in range(m)]
    assert len(letter_vertex_pairs[0]) == 2

    result = solve(ps, s, letter_vertex_pairs)
    for x in result:
        print(tf_to_yn(x))


if __name__ == '__main__':
    main()
