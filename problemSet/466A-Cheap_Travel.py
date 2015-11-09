#!/usr/bin/env python3
"""
Codeforces
466 A. Cheap Travel

@author yamaton
@date 2015-08-01
"""


def solve(n, m, a, b):
    """
    n ... # of rides needed
    m ... # of rides a special ticket provides
    a ... cost of single ride
    b ... cost of a special ticket
    """
    # if there is no discount
    if a <= b / m:
        return a * n
    else:
        special_tickets = n // m
        single_tickets = n % m
        return min(a * single_tickets + b * special_tickets, b * (special_tickets + 1))


def main():
    [n, m, a, b] = [int(i) for i in input().strip().split()]
    result = solve(n, m, a, b)
    print(result)


if __name__ == '__main__':
    main()
