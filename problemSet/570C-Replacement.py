#!/usr/bin/env python3
"""
Codeforces Round #316 (Div. 2)

Problem 570 C. Replacement

@author yamaton
@date 2015-08-13
"""

import itertools as it
import bisect
import sys

DOT = '.'
BAR = '|'


def solve(s, pairs):
    # xs is called with 1-based index. 
    n = len(s)
    # 0-th and (n+1)-th elements are guards.
    xs = [BAR] + [DOT if c == DOT else BAR for c in s] + [BAR]
    idx_char_pairs = [(int(x), DOT if c == DOT else BAR) for (x, c) in pairs]  # 1-based index
    counts = [sum(1 for _ in iterable) for c, iterable in it.groupby(xs) if c == DOT]
    total = sum(counts) - len(counts)
    n = len(xs)
    # print_stderr(''.join(xs), total)

    result = []
    for idx, c in idx_char_pairs:
        # print_stderr('At idx {}: {} -> {}'.format(idx, xs[idx], c))
        if xs[idx] == c:                          # no change
            pass
        elif xs[idx] == DOT:     # . -> |
            xs[idx] = BAR
            if xs[idx - 1] ==  xs[idx + 1] == DOT:  
                #  ... -> .|.
                total -= 2
            elif xs[idx - 1] == DOT or xs[idx + 1] == DOT:  
                #  |.. -> ||.
                total -= 1
            else:
                # |.|  ->  |||
                pass

        elif xs[idx] == BAR:       # | -> .
            xs[idx] = DOT
            if xs[idx - 1] == xs[idx + 1] == DOT:
                # .|.  -> ...
                total += 2
            elif xs[idx - 1] == DOT or xs[idx + 1] == DOT:
                # .|| -> ..|
                total += 1
            else:
                # ||| -> |.|
                pass

        result.append(total)
        # print_stderr(''.join(xs), total)

    return result



# -- Too slow
def solve_slow(s, pairs):
    idx_char_pairs = [(int(x) - 1, '.' if c == '.' else 'x') for (x, c) in pairs]
    ss = list(s)

    result = []
    for (idx, c) in idx_char_pairs:
        ss[idx] = c
        dot_stepss = [sum(1 for _ in iterable) for (cc, iterable) in it.groupby(ss) if cc == '.']
        out = sum(cnt - 1 for cnt in dot_stepss)
        result.append(out)
    return result


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    s = input().strip()
    assert len(s) == n
    xc_pairs = [input().strip().split() for _ in range(m)]

    # print_stderr(s)
    # print_stderr(xc_pairs)
    result = solve(s, xc_pairs)
    for x in result:
        print(x)


if __name__ == '__main__':
    main()
