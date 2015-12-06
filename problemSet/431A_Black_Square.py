"""
Codeforces Round #247 (Div. 2)

Problem 431 A. Black Square

@author yamaton
@date 2015-12-01
"""

def solve(xs, ys):
    d = dict(enumerate(xs, 1))
    return sum(d[y] for y in ys)

def main():
    xs = [int(c) for c in input().split()]
    ys = [int(c) for c in input()]
    result = solve(xs, ys)
    print(result)


if __name__ == '__main__':
    main()
