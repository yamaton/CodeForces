#!/usr/bin/env python3
"""
Codeforces
471 A. MUH and Sticks

@author yamaton
@date 2015-08-03
"""
import collections

def solve(xs):
    counts = tuple(sorted(collections.Counter(xs).values()))
    if counts == (2, 4) or counts == (6,):
        return 'Elephant'
    elif counts == (1, 1, 4) or counts == (1, 5):
        return 'Bear'
    else:
        return 'Alien'


def main():
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == 6
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
