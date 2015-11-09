#!/usr/bin/env python3
"""
Codeforces
559 A. Gerald's Hexagon

@author yamaton
@date 2015-08-05
"""

import sys



def solve(xs):
    pass


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

 
def main():
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == 6
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
