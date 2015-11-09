"""
Codeforces Round #328 (Div. 2)

Problem 592 A. PawnChess

@author yamaton
@date 2015-10-31
"""

import sys


def solve(board):
    board_trans = [''.join(r) for r in zip(*board)]
    # print_stderr(board_trans)
    white_steps = 10
    black_steps = 10
    for row in board_trans:
        if 'W' in row and 'B' in row:
            white_left = row.find('W')
            black_left = row.find('B')
            white_right = row.rfind('W')
            black_right = row.rfind('B')
            if white_left < black_left:
                white_steps = min(white_steps, white_left)
            if white_right < black_right:
                black_steps = min(black_steps, 7 - black_right)

        elif 'W' in row:
            white_left = row.find('W')
            white_steps = min(white_steps, white_left)

        elif 'B' in row:
            black_right = row.rfind('B')
            black_steps = min(black_steps, 7 - black_right)

        print_stderr('(W, B)', white_steps, black_steps)

    if white_steps <= black_steps:
        return 'A'
    else:
        return 'B'


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    board = [input().strip() for _ in range(8)]
    assert len(board[0]) == 8
    result = solve(board)
    print(result)


if __name__ == '__main__':
    main()
