#!/usr/bin/env python3
"""
Codeforces
510 A. Fox and Snake

@author yamaton
@date 2015-07-30
"""


def solve(n, m):
    grid = [['.'] * m for _ in range(n)]
    for i in range(0, n, 2):
        grid[i] = '#' * m

    for i in range(1, n, 2):
        if i % 4 == 1:
            grid[i][-1] = '#'
        elif i % 4 == 3:
            grid[i][0] = '#'

    return '\n'.join(''.join(xs) for xs in grid)


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    assert n % 2 == 1
    result = solve(n, m)
    print(result)


if __name__ == '__main__':
    main()
