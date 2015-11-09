"""
Codeforces
208 A. Dubstep

@author yamaton
@date 2015-07-29
"""
import sys


def solve(s):
    return ' '.join(w for w in s.split('WUB') if w)


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    s = input().strip()
    result = solve(s)
    print(result)


if __name__ == '__main__':
    main()
