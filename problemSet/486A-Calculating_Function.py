#!/usr/bin/env python3
"""
Codeforces
486 A. Calculating Function

@author yamaton
@date 2015-07-28
"""


def solve_bruteforce(n):
    return sum((-1)**i * i for i in range(1, n+1))


def solve(n):
    k = n // 2
    if n % 2 == 0:
        return k
    else:
        return k - n


def test():
    import random
    for _ in range(100):
        k = random.randint(1, 100000)
        assert solve(k) == solve_bruteforce(k)


def main():
    n = int(input())
    result = solve(n)
    print(result)


if __name__ == '__main__':
    main()
