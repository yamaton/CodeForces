"""
Codeforces Round #334 (Div. 2)

Problem 604 B. More Cowbell

@author yamaton
@date 2015-12-01
"""


def solve(xs, n, k):
    # assert xs is sorted
    if k >= n:
        return xs[-1]
    ys1 = xs[:n - k]
    ys2 = xs[n - k : 2*(n - k)]
    maxval = max(a + b for (a, b) in zip(ys1, reversed(ys2)))
    return max(maxval, xs[-1])


# def pp(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n, k = map(int, input().split())
    xs = [int(c) for c in input().split()]
    assert len(xs) == n
    result = solve(xs, n, k)
    print(result)


if __name__ == '__main__':
    main()
