"""
Codeforces Round #328 (Div. 2)

Problem 592 B. The Monster and the Squirrel

@author yamaton
@date 2015-10-31
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(n):
    count = 1
    for i in range(1, n+1):
        if i in (1, 2, n):
            count += n - 3
        else:
            count += n - 4
    return count


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    result = solve(n)
    # print_stderr(result)
    print(result)


if __name__ == '__main__':
    main()
