#!/usr/bin/env python3
"""
Codeforces
513 A. Game

@author yamaton
@date 2015-08-02
"""


def solve(n1, n2, k1, k2):
    return n1 > n2


def tf_to_msg(tf):
    return 'First' if tf else 'Second'


def main():
    [n1, n2, k1, k2] = [int(i) for i in input().strip().split()]
    result = solve(n1, n2, k1, k2)
    print(tf_to_msg(result))


if __name__ == '__main__':
    main()
