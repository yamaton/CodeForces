#!/usr/bin/env python3
"""
Codeforces
520 A. Pangram

@author yamaton
@date 2015-08-02
"""

import string

def is_pangram(s):
    return len(set(s.lower())) == len(string.ascii_lowercase)

def tf_to_yn(tf):
    return 'YES' if tf else 'NO'

def main():
    n = int(input())
    s = input().strip()
    assert len(s) == n
    result = is_pangram(s)
    print(tf_to_yn(result))


if __name__ == '__main__':
    main()
