#!/usr/bin/env python3
"""
Codeforces
476 A. Dreamoon and Stairs

@author yamaton
@date 2015-08-04
"""

# minimal number of moves to reach steps `n` s.t. 
# (1) each move is either 1 or 2 steps 
# (2) # of moves is multiple of `m`
# Return -1 if impossible

# Constraints:
#   2a + b == n
#   (a + b) % m == 0
# Find minimum moves a + b > 0

# Let m k = a + b
# Then m k + a == n
# maximal a gives the minimal k, which is k == 1
# 
def solve(n, m):
    if n < m:
        return -1

    x = (n + 1) // 2   # x: minimal steps without the multiple constraingt
    if x % m == 0:
        return x
    else:
        return x + (m - x % m)
    

def main():
    [n, m] = [int(i) for i in input().strip().split()]
    result = solve(n, m)
    print(result)


if __name__ == '__main__':
    main()
