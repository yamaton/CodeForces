#!/usr/bin/env python3
"""
Codeforces
448 A. Rewards

@author yamaton
@date 2015-07-30
"""


def solve(xs, ys, n):
    cups = sum(xs)
    medals = sum(ys)
    shelves_needed = (cups + 4) // 5 + (medals + 9) // 10
    return shelves_needed <= n


def tf_to_yn(tf):
    return 'YES' if tf else 'NO'


def main():
    xs = [int(i) for i in input().strip().split()]
    ys = [int(i) for i in input().strip().split()]
    n = int(input())
    assert len(xs) == len(ys) == 3
    result = tf_to_yn(solve(xs, ys, n))
    print(result)


if __name__ == '__main__':
    main()
