"""
Codeforces Round #330 (Div. 2)

Problem 595 B. Pasha and Phone

@author yamaton
@date 2015-11-08
"""

BASE = 1000000007

def count(k, a, b):
    # automatically takes care of the case a=0
    # (due to truncation toward negative infinity)
    x = count_multiples(a, 0, 10**k - 1)
    y = count_multiples(a, b * 10**(k-1), (b + 1) * 10**(k-1) - 1)
    return  x - y


def count_multiples(a, _from, _to):
    return _to // a - (_from - 1) // a


def solve(xs, ys, n, k):
    result = 1
    for (a, b) in zip(xs, ys):
        result = (result * count(k, a, b)) % BASE
    return result


def main():
    [n, k] = [int(i) for i in input().strip().split()]
    xs = [int(i) for i in input().strip().split()]
    ys = [int(i) for i in input().strip().split()]
    assert len(xs) == len(ys) == n // k
    result = solve(xs, ys, n, k)
    print(result)


if __name__ == '__main__':
    main()
