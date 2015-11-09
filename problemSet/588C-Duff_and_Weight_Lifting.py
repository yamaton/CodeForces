"""
Codeforces Round #326 (Div. 2)

Problem 588 C. Duff and Weight Lifting

@author yamaton
@date 2015-10-27
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs):
    """worst-case time complexity is ...
    when xs is a list of identical elements, 
     """
    counter = collections.Counter(xs)
    for x, cnt in counter.items():
        while x in bag:
            bag.remove(x)
            x += 1
        bag.add(x)
    return len(bag)




def solve(xs):
    "worst-case time complexity ... n log n if removal takes log n"
    bag = set()
    for x in sorted(xs):
        while x in bag:
            bag.remove(x)
            x += 1
        bag.add(x)
    return len(bag)


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
