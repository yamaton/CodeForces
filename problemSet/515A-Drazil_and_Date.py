#!/usr/bin/env python3
"""
Codeforces
515 A. Drazil and Date

@author yamaton
@date 2015-08-04
"""


def solve(a, b, s):
    manhattan_distance = abs(a) + abs(b)
    return s >= manhattan_distance and (s - manhattan_distance) % 2 == 0


def tf_to_yn(tf):
    return 'Yes' if tf else 'No'


def main():
    [a, b, s] = [int(i) for i in input().strip().split()]
    result = tf_to_yn(solve(a, b, s))
    print(result)


if __name__ == '__main__':
    main()
