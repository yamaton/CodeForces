#!/usr/bin/env python3
"""
Codeforces
439 A. Devu, the Singer and Churu, the Joker

@author yamaton
@date 2015-08-04
"""


def solve(ts, d):
    k = len(ts) - 1
    sum_ts = sum(ts)
    minimum_event = sum_ts + 10 * k
    if d < minimum_event:
        return -1
    else:
        return 2 * k + (d - minimum_event) // 5

def main():
    [n, d] = [int(i) for i in input().strip().split()]
    ts = [int(i) for i in input().strip().split()]
    assert len(ts) == n
    result = solve(ts, d)
    print(result)


if __name__ == '__main__':
    main()
