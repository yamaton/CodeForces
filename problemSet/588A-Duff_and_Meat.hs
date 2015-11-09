--
--Codeforces Round #326 (Div. 2)

--Problem 588 A. Duff and Meat

--@author yamaton
--@date 2015-10-26
--

solve :: [(Int, Int)] -> Int

def solve2(pairs):
    """
    O(n log n)
    """
    n = len(pairs)
    amounts, prices = list(zip(*pairs))
    price_day_pairs = sorted((p, i) for (i, p) in enumerte(prices))
    cost = 0
    last_day = n
    for (p, i) in price_day_pairs:
        if i < last_day:
            cost += p * a[i:last_day]
            i = last_day
        if i == 0:
            break
    return cost


def solve(pairs):
    """
    O(n^2) solution
    """
    n = len(pairs)
    amounts, prices = list(zip(*pairs))
    cost = 0

    while n > 0:
        day, min_price = min(enumerate(prices[:n]), key=operator.itemgetter(1))
        cost += min_price * sum(amounts[day:n])
        n = day
    return cost


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    pairs = [[int(i) for i in input().strip().split()] for _ in range(n)]
    result = solve2(pairs)
    print(result)


if __name__ == '__main__':
    main()
