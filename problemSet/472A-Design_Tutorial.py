#!/usr/bin/env python3
"""
Codeforces
472 A. Design Tutorial: Learn from Math
http://codeforces.com/problemset/problem/472/A

@author yamaton
@date 2015-07-28
"""


def two_composite_numbers(n):
    if n % 2 == 0:
        return (4, n - 4)
    elif n < 18:
        return (n - 9, 9)
    else:
        return (9, n - 9)


def main():
    n = int(input())
    result = two_composite_numbers(n)
    print(' '.join(str(i) for i in result))

if __name__ == '__main__':
    main()
