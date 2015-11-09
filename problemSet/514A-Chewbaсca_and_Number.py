#!/usr/bin/env python3
"""
Codeforces
514 A. Chewbaсca and Number

@author yamaton
@date 2015-08-04
"""
import functools


def integerdigits(n):
    """Construct list of decimal digits from the integer n

    >>> integerdigits(235)
    [2, 3, 5]
    """
    return [int(i) for i in str(n)]


def fromdigits(xs):
    """Constructs an integer from the list of decimal digits.

    >>> fromdigits([1, 9, 4, 2])
    1942
    """
    return functools.reduce(lambda i, j: 10 * i + j, xs)


def solve(x):
    def _invert(k):
        return k if k < 5 else (9 - k)

    digits = integerdigits(x)
    if digits[0] == 9:
        return fromdigits([9] + [_invert(d) for d in digits[1:]])
    else:
        return fromdigits(map(_invert, digits))


def main():
    x = int(input())
    result = solve(x)
    print(result)


if __name__ == '__main__':
    main()
