"""
Codeforces
25 A. IQ Test

@author yamaton
@date 2015-08-04
"""

# The description "evenness" is just terrible!
def solve(xs):
    odds = [i for i, x in enumerate(xs, 1) if x % 2 == 1]
    evens = [i for i, x in enumerate(xs, 1) if x % 2 == 0]
    if len(odds) == 1:
        return odds[0]
    elif len(evens) == 1:
        return evens[0]
    else:
        raise TypeError('wrong input!')


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert n == len(xs)
    result = solve(xs)
    print(result)


if __name__ == '__main__':
    main()
