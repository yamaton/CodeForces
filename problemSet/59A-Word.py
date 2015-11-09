#!/usr/bin/env python3
"""
Codeforces
59 A. Word

@author yamaton
@date 2015-08-04
"""

def solve(s):
    uppercase_length = sum(1 for c in s if c.isupper())
    lowercase_length = len(s) - uppercase_length
    if lowercase_length >= uppercase_length:
        return s.lower()
    else:
        return s.upper()


def main():
    s = input().strip()
    result = solve(s)
    print(result)


if __name__ == '__main__':
    main()
