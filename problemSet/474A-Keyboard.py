#!/usr/bin/env python3
"""
Codeforces
474 A. Keyboard

@author yamaton
@date 2015-08-02
"""


def solve(direction, chars):
    keyboard = ['qwertyuiop', 'asdfghjkl;', 'zxcvbnm,./']
    out = []
    if direction == 'R':
        diff = -1
    elif direction == 'L':
        diff = 1
    else:
        raise TypeError('wrong direction: {}'.format(direction))

    for c in chars:
        i = next(i for i, line in enumerate(keyboard) if c in line)
        k = keyboard[i].index(c)
        out.append(keyboard[i][k+diff])
    return ''.join(out)


def main():
    direction = input().strip()
    chars = input().strip()
    assert direction == 'L' or direction == 'R'
    result = solve(direction, chars)
    print(result)


if __name__ == '__main__':
    main()
