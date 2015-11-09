#!/usr/bin/env python3
"""
Codeforces
500 A. New Year Transportation

@author yamaton
@date 2015-07-29
"""
import sys
import operator


def solve(xs, n, t):
    dest = list(map(operator.add, range(1, n), xs))
    if t == 1:
        return True

    pos = 1
    while pos < t:
        pos = dest[pos - 1]
        if pos == t:
            return True
    else:
        return False


def tf_to_yn(tf):
    return 'YES' if tf else 'NO'


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, t] = [int(i) for i in input().strip().split()]
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n - 1
    result = tf_to_yn(solve(xs, n, t))
    print(result)


if __name__ == '__main__':
    main()
