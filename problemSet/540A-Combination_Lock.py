#!/usr/bin/env python3
"""
Codeforces
540 A. Combination Lock

@author yamaton
@date 2015-08-04
"""


def digit_distance(a, b):
    a, b  = min(a, b), max(a, b)
    dist1 = b - a
    dist2 = 10 + a - b
    return min(dist1, dist2)


def solve(goal, current):
    return sum(digit_distance(a, b) for (a, b) in zip(goal, current))


def main():
    n = int(input())
    original = [int(c) for c in input().strip()]
    mcduck = [int(c) for c in input().strip()]
    assert n == len(original) == len(mcduck)
    result = solve(original, mcduck)
    print(result)


if __name__ == '__main__':
    main()
