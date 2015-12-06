"""
Codeforces Round #331 (Div. 2)

Problem 596 D. Wilbur and Trees

@author yamaton
@date 2015-11-15
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

def is_overlapping(s1, s2):
    return not (max(s1) < min(s2) or max(s2) < min(s1))


def merge_intervals(segs):
    segs.sort()
    stack = []
    stack = [segs[0]]
    for s in segs[1:]:
        r = stack[-1]
        if is_overlapping(s, r):
            r = stack.pop()
            interval = (min(s[0], r[0]), max(s[1], r[1]))
            stack.append(interval)
        else:
            stack.append(s)
    return stack


def interval_sum(segs):
    return sum(b - a for (a, b) in merge_intervals(segs))


def add(segs, s):
    return segs + [s]

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)


def solve(xs, n, h, p):

    def cascade_right(trees):
        return sum(1 for _ in it.takewhile(lambda tup: tup[1] - tup[0] < h, pairwise(trees)))

    def cascade_left(trees):
        return cascade_right(reversed(trees))

    def covered(segments, trees):
        if not trees:
            return interval_sum(segments)
        else :
            nn = len(trees)

            llseg = add(segments, (trees[0] - h, trees[0]))
            ll = covered(llseg, trees[1:])

            rrseg = add(segments, (trees[-1], trees[-1] + h))
            rr = covered(rrseg, trees[:-1])

            if nn == 1:
                return p * ll + (1-p) * rr

            idx = cascade_right(trees, h)
            lrseg = add(segments, (trees[0], trees[idx] + h))
            lr = covered(lrseg, trees[idx+1:])

            idx = cascade_left(trees, h)
            rlseg = add(segments, (trees[nn-idx-1] - h, trees[-1]))
            rl = covered(rlseg, trees[:(nn-idx-1)])

            return 0.5 * (p * (ll + rl) + (1 - p) * (lr + rr))

    xs.sort()
    return covered([], xs)


def pp(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def main():
    [n, h, p] = input().strip().split()
    [n, h] = map(int, [n, h])
    p = float(p)
    xs = [int(_c) for _c in input().strip().split()]
    result = solve(xs, n, h, p)
    print("%.9f" % result)


if __name__ == '__main__':
    main()
