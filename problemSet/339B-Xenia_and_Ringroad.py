#!/usr/bin/env python3
"""
Codeforces
339 B. Xenia and Ringroad

@author yamaton
@date 2015-08-04
"""

def solve(n, xs):
    def house_distance(a, b):
        return (b - a) % n

    return sum(house_distance(a, b) for (a, b) in zip([1] + xs,xs)) 


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    xs = [int(i) for i in input().strip().split()]
    assert m == len(xs)
    assert all(1 <= a <= n for a in xs)
    result = solve(n, xs)
    print(result)


if __name__ == '__main__':
    main()
