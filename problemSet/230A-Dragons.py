"""
Codeforces
230 A. Dragons

@author yamaton
@date 2015-08-04
"""

def solve(strength, xs):
    for (dragon_strength, bonus) in sorted(xs):
        if strength > dragon_strength:
            strength += bonus
        else:
            return False
    else:
        return True


def tf_to_yn(tf):
    return 'YES' if tf else 'NO'

def main():
    [strength, n] = [int(i) for i in input().strip().split()]
    xys = [tuple(int(i) for i in input().strip().split()) for _ in range(n)]
    result = tf_to_yn(solve(strength, xys))
    print(result)


if __name__ == '__main__':
    main()
