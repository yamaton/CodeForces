#!/usr/bin/env python3
"""
Codeforces
519 A. A and B and Chess

@author yamaton
@date 2015-08-02
"""

import string

WEIGHT = {'Q': 9, 'R': 5, 'B': 3, 'N': 3, 'P': 1, 'K': 0}

def weight(c):
    x = c.upper()
    return WEIGHT[x]

def solve(board):
    s = ''.join(board)
    white = sum(weight(c) for c in s if c.isupper())
    black = sum(weight(c) for c in s if c.islower())

    if white > black:
        return 'White'
    elif white == black:
        return 'Draw'
    else:
        return 'Black'


def main():
    board = [input().strip() for _ in range(8)]
    assert len(board[0]) == 8
    result = solve(board)
    print(result)


if __name__ == '__main__':
    main()
