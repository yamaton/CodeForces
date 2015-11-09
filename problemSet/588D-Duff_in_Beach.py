"""
Codeforces Round #326 (Div. 2)

Problem 588 D. Duff in Beach

@author yamaton
@date 2015-10-27
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

def solve(xs, n, l, k):
    ""
    pass


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, l, k] = [int(i) for i in input().strip().split()]
    xs = [int(i) for i in input().strip().split()]    
    assert len(xs) == n
    result = solve(xs, n, l, k)
    print(result)


if __name__ == '__main__':
    main()
