#!/usr/bin/env python3
"""
Codeforces
509 A. Maximum in Table

@author yamaton
@date 2015-08-02
"""

import string

def solve(n):
    """
    a[i, 1] = a[1, i] = 1
    a[i, j] = a[i-1, j] + a[i, j-1]

    a[n, n] = 
    """
    mat = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        mat[0][i] = 1
        mat[i][0] = 1

    for i in range(1, n):
        for j in range(1, n):
            mat[i][j] = mat[i-1][j] + mat[i][j-1]
    return mat[n-1][n-1]


def main():
    n = int(input())
    result = solve(n)
    print(result)


if __name__ == '__main__':
    main()
