#!/usr/bin/env python3
"""
Codeforces
568 A. Primes or Palindromes

@author yamaton
@date 2015-08-10
"""

import itertools
import math

def is_palindrome(number):
    """Check if number is palindrome, the numbers identical to its reversed-direction digits.

    >>> is_palindrome(15651)
    True

    >>> is_palindrome(56)
    False

    >>> is_palindrome('abcba')
    True
    """
    s = str(number)
    return s == ''.join(reversed(s))



def is_prime(n):
    """
    Return True if the integer n is prime.

    >>> is_prime(391)
    False

    >>> is_prime(397)
    True

    See also sympy.ntheory.isprime
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    max_p = int(math.sqrt(n))
    return all(n % p != 0 for p in range(3, max_p + 1, 2))


def solve(p, q):
    counter = itertools.count(1)
    pi = 0
    rub = 0
    for n in counter:
        if is_prime(n):
            pi += 1
        if is_palindrome(n):
            rub += 1
        if q * pi > p * rub:
            return n - 1, (pi, rub)


def tf_to_msg(n):
    if n is None:
        return 'Palindromic tree is better than splay tree'
    else:
        return str(n)


def main():
    [p, q] = [int(i) for i in input().strip().split()]
    result = solve(p, q)
    print(result)


if __name__ == '__main__':
    main()
