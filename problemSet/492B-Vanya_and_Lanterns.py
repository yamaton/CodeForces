#!/usr/bin/env python3
"""
Codeforces Round #280 (Div 2)
492 B. Vanya and Lanterns

@author yamaton
@date 2015-11-03
"""


def solve_bruteforce(xs, l):
    xs.sort()
    if len(xs) > 1:
        most = max(b - a for (a, b) in zip(xs, xs[1:])) / 2
        return max(most, xs[0] - 0, l - xs[-1])
    else:
        return max(xs[0])


def main():
    [n, l] = [int(i) for i in input().strip().split()]
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    result = solve_bruteforce(xs, l)
    print(result)


if __name__ == '__main__':
    main()
