#!/usr/bin/env python3
"""
Codeforces
455 A. Boredom

@author yamaton
@date 2015-08-22
      2015-09-10
      2015-09-22
"""

import collections

def solve(xs):
    cnt = collections.Counter(xs)
    xmax = max(xs)

    f = collections.defaultdict(int)
    # Let f[k] be the maximum point from sequence of selected integers such that
    # elements of the sequence are all in range [1, k], and **k is selected**.
    for i in range(1, xmax+1):
        f[i] = max(f[i-1], cnt[i] * i + f[i-2])

    return f[xmax]

def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
