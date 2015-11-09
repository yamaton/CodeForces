"""
Codeforces Round #330 (Div. 2)

Problem 595 D. Max and Bike

@author yamaton
@date 2015-11-08
"""

import math
import sys



sys.setrecursionlimit(10000000)


def solve_for_t(r, v, l):
    xp = l % (2 * math.pi * r)

    def f(t):
        return v * t + 2 * r * math.sin(v * t / (2 * r)) - xp

    def dfdt(t):
        return v * (1 + math.cos(v * t))

    def newton(t):
        return t - f(t) / dfdt(t)


    t0 = (l - xp) / v
    prev = 1.0
    t = newton(prev)
    while abs(t - prev) > 0.000001 or abs(t - prev) / max(1, abs(t)) > 0.000001:
        print(' .... t =', t, file=sys.stderr)
        prev, t = t, newton(t)

    print('t0 =', t0, file=sys.stderr)
    print('t =', t, file=sys.stderr)
    print('prev =', prev, file=sys.stderr)

    print('left(t1) =', v * t + 2 * r * math.sin(v * t / (2 * r)), file=sys.stderr)
    print('f(t1) =', f(t), file=sys.stderr)
    print('xp =', xp, file=sys.stderr)
    print('result =', t + t0)

    return t0 + t


def solve(pairs, r, v):
    distances = [(f - s) for (s, f) in pairs]
    return [solve_for_t(r, v, d) for d in distances]


def main():
    [n, r, v] = [int(i) for i in input().strip().split()]
    pairs = [[int(i) for i in input().strip().split()] for _ in range(n)]
    results = solve(pairs, r, v)
    for res in results:
        print(res)


if __name__ == '__main__':
    main()
