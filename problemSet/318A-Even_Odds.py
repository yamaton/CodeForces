#!/usr/bin/env python3
"""
Codeforces
318 A. Even Odds

@author yamaton
@date 2015-07-31
"""


def solve(n, k):
    first_half = (n + 1) // 2
    if k <= first_half:
        return 2 * k - 1
    else:
        return 2 * (k - first_half)

def main():
    [n, k] = [int(i) for i in input().strip().split()]
    result = solve(n, k)
    print(result)


if __name__ == '__main__':
    main()
