"""
Codeforces Round 333 (Div. 2)

Problem 601 A. / 602 C. The Two Routes

@author yamaton
@date 2015-11-24
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

def reachable(start, goal, adjlist):
    q = collections.deque()
    q.append(start)
    visited = {start}
    while q:
        town = q.popleft()
        if town == goal:
            return True
        for tn in adjlist[town]:
            if tn not in visited:
                q.append(tn)
                visited.add(tn)
    return False


def to_adjlist(pairs):
    d = collections.defaultdict(set)
    for (i, j) in pairs:
        d[i].add(j)
        d[j].add(i)
    return d


def solve(pairs, n, m):
    rails = to_adjlist(pairs)
    nodes = set(range(1, n+1))
    buses = {i: (nodes - rails[i]) for i in range(1, n+1)}

    if not (reachable(1, n, rails) and reachable(1, n, buses)):
        return -1

    q = collections.deque()
    q.append((1, 1, 0))

    while q:
        # pp(q)
        r, b, time = q.popleft()
        for rn in rails[r]:
            for bn in buses[b]:
                # pp('time:', time, '  rail:', r, '->', rn, '   bus:', b, '->', bn)
                if rn == bn == n:
                    return time + 1
                elif rn == bn:
                    continue
                q.append((rn, bn, time + 1))

    return "Something is wrong!"



def pp(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def main():
    [n, m] = map(int, input().strip().split())
    pairs = [tuple(int(_c) for _c in input().strip().split()) for _ in range(m)]
    result = solve(pairs, n, m)
    print(result)


if __name__ == '__main__':
    main()
