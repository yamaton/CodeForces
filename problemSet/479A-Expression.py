#!/usr/bin/env python3
"""
Codeforces
479 A. Expression

@author yamaton
@date 2015-07-29
"""
import operator
import itertools


def fold(fs, xs):
    acc = xs[0]
    assert len(fs) + 1 == len(xs)
    for x, f in zip(xs[1:], fs):
        acc = f(acc, x)
    return acc


def solve(a, b, c):
    # you cannot change the order, but + and * are commutative.
    # (b, c, a) should read order for f(a, g(b, c))
    orders = [(a, b, c), (b, c, a)]
    operators = itertools.combinations_with_replacement(
                    [operator.add, operator.mul], 2)
    return max(fold(ops, args) for ops in operators for args in orders)


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    result = solve(a, b, c)
    print(result)


if __name__ == '__main__':
    main()
