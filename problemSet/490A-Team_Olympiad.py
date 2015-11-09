#!/usr/bin/env python3
"""
Codeforces
490 A. Team Olympiad

@author yamaton
@date 2015-08-04
"""


def solve(xs):
    mathematicians = [i for i, x in enumerate(xs, 1) if x == 1]
    programmers = [i for i, x in enumerate(xs, 1) if x == 2]
    sportsmen = [i for i, x in enumerate(xs, 1) if x == 3]
    return list(zip(mathematicians, programmers, sportsmen))


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    troikas = solve(xs)
    print(len(troikas))
    for troika in troikas:
        print(' '.join(str(k) for k in troika))


if __name__ == '__main__':
    main()
