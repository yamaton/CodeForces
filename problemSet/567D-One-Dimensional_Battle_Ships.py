#!/usr/bin/env python3
"""
Codeforces
567 D. One-Dimensional Battle Ships

@author yamaton
@date 2015-08-05
"""

import sys
import bisect


def solve(xs, field_length, num_ships, ship_length):
    def num_accomodate(size):
        return (size + 1) // (ship_length + 1)

    bombed = [0, field_length+1]
    holes = [field_length]

    for i, x in enumerate(xs, 1):
        pos = bisect(bombed, x)

        holes = bomed[max(q - p - 1, 0) for (p, q) in zip(h, h[1:])]
        ss = sum(map(num_accomodate, holes))
        print_stderr(i, ss, h)
        if ss < num_ships:
            return i
    return -1


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

 
def main():
    [n, k, a] = [int(i) for i in input().strip().split()]    
    m = int(input())
    xs = [int(i) for i in input().s    trip().split()]
    assert len(xs) == m
    result = solve(xs, n, k, a)
    print(result)


if __name__ == '__main__':
    main()
