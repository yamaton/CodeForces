#!/usr/bin/env python3
"""
Codeforces
507 A. Amr and Music

@author yamaton
@date 2015-08-04
"""
import operator

def solve(xs, k):
    if k == 0:
        return []

    indexed_xs = list(enumerate(xs, 1))
    indexed_xs.sort(key=operator.itemgetter(1))
    acc = 0
    result = []
    for i, x in indexed_xs:
        acc += x
        if acc <= k:
            result.append(i)
        else:
            break
    return sorted(result)


def main():
    [n, k] = [int(i) for i in input().strip().split()]
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    result = solve(xs, k)
    print(len(result))
    print(' '.join(str(n) for n in result))


if __name__ == '__main__':
    main()
