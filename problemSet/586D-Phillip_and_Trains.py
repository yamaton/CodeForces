"""
Codeforces Round #325 (Div. 2)

Problem 586 D. Phillip and Trains


@author yamaton
@date 2015-11-09
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def conseq_positions(xs):
    ys = [(c, sum(1 for _ in iterable)) for (c, iterable) in it.groupby(xs)]
    cs, lens = list(zip(*ys))
    positions = list(it.accumulate(lens))
    return zip(cs, [0] + positions[:-1])


def neighbors(i, j, i_max, j_max):
    return [(i+1, j), (i-1, j), (i, j + 1)]


def solve(trains, board):
    start = next((i, line.index('s')) for (i, line) in enumerate(board) if 's' in line)
    maze = [['.' if c == '.' or c == 's' else 'X' for c in line] for line in board]

    # p('\n------- before --------')
    # for line in maze:
    #     p(''.join(line))
    # p('------- ----- --------')

    row_size = len(maze)
    col_size = len(maze[0])

    for row in range(row_size):
        line = maze[row]
        positions = conseq_positions(line)
        for (c, j) in positions:
            if c == '.' and j % 2 == 1:
                maze[row][j] = 'X'

    p('\n------- after --------')
    for line in maze:
        p(''.join(line))
    p('------- ----- --------')


    visited = set()
    stack = [start]
    while stack:
        (i, j) = stack.pop()
        visited.add((i, j))
        if j == col_size - 1:
            p('goal =', (i, j))
            return True
        nexts = neighbors(i, j, row_size, col_size)
        for (ni, nj) in nexts:
            if (0 <= ni < row_size and 0 <= nj < col_size and
                (ni, nj) not in visited and maze[ni][nj] == '.'):
                stack.append((ni, nj))

    return False


def tf_to_yn(tf):
    return 'YES' if tf else 'NO'


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)

def main():
    t = int(input())
    for _ in range(t):
        [n, k] = [int(i) for i in input().strip().split()]
        board = [input().strip() for _ in range(3)]
        assert len(board[0]) == n
        result = solve(k, board)
        print(tf_to_yn(result))



if __name__ == '__main__':
    main()
