#!/usr/bin/env python3
"""
Codeforces
431 A. Black Square

@author yamaton
@date 2015-08-05
"""

def solve(xs, s):
    ys = [sum(1 for _ in ite) for (i, ite) in itertools.groupby(xs) if i == 0] 
    consecutive_zeros = max(ys) if ys else 0
    return xs.count(1) + consecutive_zeros


def main():
    xs = [int(i) for i in input().strip().split()]
    s = int(input())
    assert len(xs) == 5
    result = solve(xs, s)
    print(result)


if __name__ == '__main__':
    main()
