#!/usr/bin/env python3
"""
Codeforces
41 A. Translation

@author yamaton
@date 2015-07-28
"""


def tf_to_yn(tf):
    return 'YES' if tf else 'NO'


def solve(s, t):
    return s[::-1] == t


def main():
    s = input().strip()
    t = input().strip()
    result = solve(s, t)
    print(tf_to_yn(result))


if __name__ == '__main__':
    main()
