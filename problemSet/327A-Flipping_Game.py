"""
Codeforces Round #191 (Div. 2)
327 A. Flipping Game

@author yamaton
@date 2015-08-05
      2015-09-22
      2015-11-04
"""

import itertools
import collections
import sys

def solve_bruteforce(xs):
    "O(N^3) solution"
    n = len(xs)
    if n == 1:
        return len(xs) - sum(xs)
    return max(sum(xs[:i]) + sum(xs[j:]) - sum(xs[i:j]) + (j - i)
               for (i, j) in itertools.combinations(n, 2))


def solve_(xs):
    "O(N^2) solution"
    n = len(xs)
    assert n > 0
    a = [1 if x == 0 else -1 for x in xs]
    b = collections.defaultdict(int)
    for i, acc in enumerate(itertools.accumulate(a)):
        b[i] = acc
    deltaS = max(b[j] - b[i] for i in range(-1, n) for j in range(i+1, n))
    if deltaS <= 0:
        return sum(xs) - 1
    else:
        return sum(xs) + deltaS


def solve(xs):
    "O(N) with DP"
    a = [1 if x == 0 else -1 for x in xs]
    b = itertools.accumulate(a)
    deltaS = 0
    min_so_far = 0
    for bk in b:
        deltaS = max(deltaS, bk - min_so_far)
        min_so_far = min(min_so_far, bk)

    if deltaS == 0:
        return sum(xs) - 1
    else:
        return sum(xs) + deltaS


def test():
    xs = [0]
    assert solve(xs) == 1
    xs = [1]
    assert solve(xs) == 0
    xs = [0, 1, 0]
    assert solve(xs) == 2
    xs = [0, 0, 1, 0, 0]
    assert solve(xs) == 4
    xs = [0, 0, 0, 0]
    assert solve(xs) == 4
    xs = [1, 1, 1]
    assert solve(xs) == 2




def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
