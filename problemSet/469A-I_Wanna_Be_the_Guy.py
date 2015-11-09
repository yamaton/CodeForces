#!/usr/bin/env python3
"""
Codeforces
492 A. Vanya and Cubes

@author yamaton
@date 2015-07-29
"""


def solve(xs, ys, n):
    return (set(xs) | set(ys)) == set(range(1, n+1))


def tf_to_message(tf):
    if tf:
        return 'I become the guy.'
    else:
        return 'Oh, my keyboard!'


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    ys = [int(i) for i in input().strip().split()]
    assert xs[0] == len(xs[1:])
    assert ys[0] == len(ys[1:])

    result = solve(xs[1:], ys[1:], n)
    print(tf_to_message(result))


if __name__ == '__main__':
    main()
