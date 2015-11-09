#!/usr/bin/env python3
"""
Codeforces Round #316 (Div. 2)

Problem A. Elections

@author yamaton
@date 2015-08-13
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def process1(xs):
    """
    process1 :: [VoteCount] -> Candidate
    where Candidate is Index of the array
    """
    # candidate is 1-based index
    return max(enumerate(xs, 1), key=operator.itemgetter(1))[0]

def process2(xs):
    """
    process2 :: [Candidate] -> Candidate
    where City is Index of the array
    """
    counts = [(xs.count(x), x) for x in set(xs)]
    return max(counts)[1]


def solve(xss):
    print_stderr(xss)
    first_round = [process1(xs) for xs in xss]
    print_stderr(first_round)
    second_round = process2(first_round)
    return second_round


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    xss = [[int(i) for i in input().strip().split()] for _ in range(m)]
    assert len(xss[0]) == n

    result = solve(xss)
    print(result)


if __name__ == '__main__':
    main()