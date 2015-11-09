"""
Codeforces Round #325 (Div. 2)

Problem 586 C. Gennady the Dentist


@author yamaton
@date 2015-11-09
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(triples):
    vs, ds, ps = list(zip(*triples))

    def queue_map(state):
        if not state:
            return []

        rest = state[1:]
        treated, _ = state[0]
        v = vs[treated]

        fleeing = set()
        n = len(rest)
        for k in range(v):
            if k < n:
                rest[k][1] -= v - k
                if rest[k][1] < 0:
                    fleeing.add(rest[k][0])
            else:
                break

        for k in range(len(rest)):
            this_id = rest[k][0]
            if this_id in fleeing:
                continue
            rest[k][1] -= sum(ds[child_id] for child_id in fleeing if child_id < this_id)
            if rest[k][1] < 0:
                fleeing.add(rest[k][0])

        return treated, [[i, p] for (i, p) in rest if i not in fleeing]


    state = [[i, p] for i, p in enumerate(ps)]
    result = []
    while state:
        i, state = queue_map(state)
        result.append(i + 1)
    return result


def main():
    n = int(input())
    vdp_triples = [[int(i) for i in input().strip().split()] for _ in range(n)]
    assert len(vdp_triples[0]) == 3
    result = solve(vdp_triples)
    print(len(result))
    print(' '.join(str(n) for n in result))


if __name__ == '__main__':
    main()
