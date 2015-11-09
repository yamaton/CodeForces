"""
Codeforces Round #327 (Div. 2)

Problem 591 B. Rebranding

@author yamaton
@date 2015-11-06
"""

import string
import sys


def solve(s, pairs):
    """
    O(Σ + N + M)
    :para   m s: string of length M
    :param pairs: [(char, char)] of length N
    :return: string
    """
    origin_of = {c: c for c in string.ascii_lowercase}
    for (c1, c2) in pairs:
        origin_of[c1], origin_of[c2] = origin_of[c2], origin_of[c1]

    d = {v: k for k, v in origin_of.items()}
    return ''.join(d[c] for c in s)



def solve0(s, pairs):
    """
    O(Σ M + N)
    :param s:
    :param pairs:
    :return:
    """
    d = {c: c for c in string.ascii_lowercase}
    for (c1, c2) in pairs:
        for c in string.ascii_lowercase:
            if d[c] == c1:
                d[c] = c2
            elif d[c] == c2:
                d[c] = c1
    return ''.join(d[c] for c in s)


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    s = input().strip()
    assert len(s) == n
    pairs = [tuple(input().strip().split()) for _ in range(m)]
    result = solve(s, pairs)
    print(result)


if __name__ == '__main__':
    main()
