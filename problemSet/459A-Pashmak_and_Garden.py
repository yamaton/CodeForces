#!/usr/bin/env python3
"""
Codeforces
459 A. Pashmak and Garden

@author yamaton
@date 2015-08-04
"""


def solve(x1, y1, x2, y2):
    if x1 == x2:
        side = abs(y2 - y1)
        x = x1 + side
        return [x, y1, x, y2] 
    elif y1 == y2:
        side = abs(x2 - x1)
        y = y1 + side
        return [x1, y, x2, y]
    elif abs(x2 - x1) == abs(y2 - y1):
        return [x1, y2, x2, y1]
    else:
        return None


def main():
    x1, y1, x2, y2 = [int(i) for i in input().strip().split()]
    result = solve(x1, y1, x2, y2)
    if result is None:
        print(-1)
    else:
        print(' '.join(str(n) for n in result))

if __name__ == '__main__':
    main()
