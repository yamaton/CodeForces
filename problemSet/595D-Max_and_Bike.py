"""
Codeforces Round #330 (Div. 2)

Problem 594 B / 595 D. Max and Bike

@author yamaton
@date 2015-11-08
"""

import math
import random
import sys

import functools


@functools.lru_cache(None)
def solve_for_t(r, v, l):
    pm = 1 if (l / 2) % (2 * math.pi * r) < math.pi * r else -1
    def f(t):
        # return v * t + 2 * pm * r * math.sin(half_omega * t) - l
        return v * t + 2 * pm * r * math.sin(v * t / (2 * r)) - l

    def dfdt(t):
        # return v * (1 + pm * math.cos(half_omega * t))
        return v * (1 + pm * math.cos(v * t / (2 * r)))

    def newton(t):
        return t - f(t) / dfdt(t)


    # p('\n----------------')
    estimate = l / v
    prev = estimate
    t = newton(prev)
    while abs(t - prev) > 0.0000001 or abs(t - prev) / max(1, abs(t)) > 0.0000001:
        if t < - estimate or t > 10 * estimate:
            t = random.random() * 2 * estimate
        # p('... t =', t)
        prev, t = t, newton(t)

    # p('prev =', prev)
    # p('left(t) =', v * t + 2 * r * math.sin(v * t / (2 * r)))
    # p('l =', l)
    # p('f(t) =', f(t))

    return t


def solve(pairs, r, v):
    distances = [(f - s) for (s, f) in pairs]
    return [solve_for_t(r, v, d) for d in distances]


def p(*args, **kwargs):
    return print(file=sys.stderr, *args, **kwargs)


def main():
    [n, r, v] = [int(i) for i in input().strip().split()]
    pairs = [[int(i) for i in input().strip().split()] for _ in range(n)]
    results = solve(pairs, r, v)
    for res in results:
        print("%.12f" % res)


if __name__ == '__main__':
    main()
