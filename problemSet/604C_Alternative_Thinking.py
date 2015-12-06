"""
Codeforces Round #334 (Div. 2)

Problem 604 C. Alternative Thinking

@author yamaton
@date 2015-12-01
"""

import itertools as it


def solve(s: str, n: int) -> int:
    lens = [sum(1 for i in iterable) for (_, iterable) in it.groupby(s)]
    maxlen = max(lens)
    altlen = len(lens)
    if maxlen == 1:
        ans = altlen
    elif maxlen >= 3:
        ans = altlen + 2
    elif lens.count(2) == 1:
        ans = altlen + 1
    else:
        ans = altlen + 2
    return ans


# def pp(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    s = input().strip()
    assert len(s) == n
    result = solve(s, n)
    print(result)


if __name__ == '__main__':
    main()
