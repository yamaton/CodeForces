"""
Codeforces
149 A.  Business trip

@author yamaton
@date 2015-08-04
"""


def solve(xs, k):
    if sum(xs) < k:
        return -1
    if k == 0:
        return 0

    ys = sorted(xs, reverse=True)
    centimeter = 0
    month = 0
    for y in ys:
        centimeter += y
        month += 1
        if centimeter >= k:
            return month


def main():
    k = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == 12
    result = solve(xs, k)
    print(result)


if __name__ == '__main__':
    main()
