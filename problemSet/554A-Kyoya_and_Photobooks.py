#!/usr/bin/env python3
"""
Codeforces Round #309 (Div. 2)

Problem 554 A. Kyoya and Photobooks

@author yamaton
@date 2015-08-17
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(s):
    letters = set(s)
    letter_count = len(letters)
    size = len(s)

    distinct_count = (26 - letter_count) * (size + 1)

    duplicates = {s[:i] + let + s[i:] for let in letters for i in range(0, size+1)}
    duplicate_count = len(duplicates)
    return distinct_count + duplicate_count


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    s = input().strip()
    result = solve(s)
    print(result)


if __name__ == '__main__':
    main()