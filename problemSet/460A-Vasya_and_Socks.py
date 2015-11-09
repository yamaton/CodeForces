#!/usr/bin/env python3
"""
Codeforces
460 A. Vasya and Socks

@author yamaton
@date 2015-07-28
"""


def solve(socks, interval):
    day = 0
    while socks:
        socks -= 1
        if day > 0 and (day + 1) % interval == 0:
            socks += 1
        day += 1
    return day


def main():
    n, m = [int(i) for i in input().split()]
    result = solve(n, m)
    print(result)


if __name__ == '__main__':
    main()
