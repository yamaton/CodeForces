"""
Codeforces Round #331 (Div. 2)

Problem 596 C Wilbur and Points

@author yamaton
@date 2015-11-15
      2015-11-21
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


# bruteforce
def solve(pairs, ws, n)
    d = collections.defaultdict(list)
    cnt = collections.defaultdict(int)
    for (x, y) in pairs:
        d[y - x].append((x, y))
        cnt[y - x] += 1

    if not cnt != collections.Counter(ws):
        return ('NO', [])

    for key in d:
        d[key] = collections.deque(sorted(d[key]))

    result = []
    for w in ws:
        point = d[w].popleft()
        result.append(point)

    max_y_upto = collections.defaultdict(int)
    for (x, y) in sorted(result, reverse=True):
        max_y_after[x] = max(max_y_after[x], y)

    for (x, y) in result:
        pass
    return result


# def p(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    pairs = [tuple(int(_c) for _c in input().strip().split()) for _ in range(n)]
    xs = [int(_c) for _c in input().strip().split()]
    assert len(xs) == n


    yn, pts = solve(pairs, xs, n)
    print(yn)
    for p in pts:
        print(*p)


if __name__ == '__main__':
    main()
