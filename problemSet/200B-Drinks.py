"""
Codeforces Round #126 (Div. 2)

Problem 200 B. Drinks

@author yamaton
@date 2015-11-20
"""
import sys


def solve(xs, n):
    return sum(xs) / n


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n

    result = solve(xs, n)
    print("%.12f" % result)


if __name__ == '__main__':
    main()
