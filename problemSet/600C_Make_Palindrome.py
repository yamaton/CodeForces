"""
Codeforces Educational Round 2

Problem 600 C. Make Palindrome

@author yamaton
@date 2015-11-30
"""

import collections


def solve(s: str) -> [str]:
    n = len(s)
    chars = collections.Counter(s)
    base = [c for c in chars if chars[c] >= 2 for _ in range(chars[c] // 2)]
    rest = sorted(c for c in chars if chars[c] % 2 == 1)
    keep = len(rest) // 2
    selected = sorted(base + rest[:keep])
    middle = rest[keep]
    middle_elem = [] if n % 2 == 0 else [middle]
    return selected + middle_elem + selected[::-1]


def main():
    s = input().strip()
    result = solve(s)
    print(''.join(result))


if __name__ == '__main__':
    main()
