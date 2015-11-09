#!/usr/bin/env python3
"""
Codeforces
427 A. Police Recruits

@author yamaton
@date 2015-08-02
"""
import functools

def solve(xs):
    def _f(acc, x):
        police_available, untreated_cases = acc
        police_available += x
        if police_available < 0:
            police_available = 0
            untreated_cases += 1
        return (police_available, untreated_cases)

    police, cnt = functools.reduce(_f, xs, (0, 0))
    return cnt

    # cnt = 0
    # acc = 0
    # for x in xs:
    #     acc += x
    #     if acc < 0:
    #         cnt += 1
    #         acc = 0
    # return acc

def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
