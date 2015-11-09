"""
Codeforces Round #327 (Div. 2)

Problem 591 C. Median Smoothing

@author yamaton
@date 2015-11-06
"""


def reduce_consec(iterable):
    """
    [1, 2, 3, 6, 7, 9, 10, 11, 12, 13, 20]
    --> [(1, 3), (6, 2), (9, 5), (20, 1)]
    Detect consecutive part and (starting_value, length) pair

    :param xs: List of int
    :return: List of pair of int
    """
    stack = []
    for x in iterable:
        if stack:
            # check if consective
            if stack[-1] + 1 == x:
                stack.append(x)
            # if not consecutive, flush stack and start with new element
            else:
                yield (stack[0], len(stack))
                stack = [x]
        else:
            # starting element
            stack.append(x)

    if stack:
        yield (stack[0], len(stack))


def alternating_indices(xs):
    for i, x in enumerate(xs):
        if i == 0 or i == len(xs) - 1:
            continue
        if xs[i-1] != x and xs[i+1] != x:
            yield i


def alternating_position_and_length(xs):
    for x in xs:
        pass



def solve(xs, n):
    # zigzag = []  # alternating part
    # for i, x in enumerate(xs):
    #     if i == 0 or i == n - 1:
    #         continue
    #     if xs[i-1] != x and xs[i+1] != x:
    #         zigzag.append(i)

    zigzag = alternating_indices(xs)
    zigzag_start_length_pairs = reduce_consec(zigzag)
    count = 0
    result = xs[:]
    for (i, n) in zigzag_start_length_pairs:
        n_half = n // 2
        count = max(count, (n + 1) // 2)
        if n % 2 == 0:
            for j in range(i, i + n_half):
                result[j] = xs[i-1]
            for j in range(i + n_half, i + n):
                result[j] = 1 - xs[i-1]
        else:
            for j in range(i, i + n):
                result[j] = xs[i-1]
    return count, result


def solve_bruteforce(xs, n):
    def transform(ps):
        result = []
        for i in range(n):
            if i == 0 or i == n-1:
                result.append(ps[i])
            else:
                median = int(sum(ps[i-1:i+2]) >= 2)
                result.append(median)
        return tuple(result)

    xs = tuple(xs)
    seen = set()
    seen.add(xs)
    ys = transform(xs)
    count = 0
    while ys != xs:
        # Actually, this system always ends up to a fixed point. No cycle exists.
        if ys in seen:
            return -1, xs
        xs = ys
        seen.add(xs)
        count += 1
        ys = transform(xs)

    return count, xs


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    count, seq = solve(xs, n)
    print(count)
    print(' '.join(str(n) for n in seq))


if __name__ == '__main__':
    main()
