"""
Codeforces
237 A. Free Cash

@author yamaton
@date 2015-08-03
"""
import collections

def solve(pairs):
    tups = [tuple(pair) for pair in pairs]
    return max(collections.Counter(tups).values())


def main():
    n = int(input())
    customer_arrivals = [[int(i) for i in input().strip().split()] for _ in range(n)]
    result = solve(customer_arrivals)
    print(result)


if __name__ == '__main__':
    main()
