"""
Codeforces Round #328 (Div. 2)

Problem 592 E. BCPC

@author yamaton
@date 2015-10-31
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(edges, attacked_nodes):
    pass


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, c, d] = [int(i) for i in input().strip().split()]
    pairs =  [tuple(int(i) for i in input().strip().split()) for _ in range(n)]
    result = solve(c, d, pairs)    
    print(result)

if __name__ == '__main__':
    main()
