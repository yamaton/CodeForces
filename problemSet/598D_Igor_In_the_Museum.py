"""
Codeforces Educational Round

Problem 598 D. Igor In the Museum

@author yamaton
@date 2015-11-12
"""
import collections


def neighbors(pos):
    i, j = pos
    yield (i+1, j)
    yield (i-1, j)
    yield (i, j-1)
    yield (i, j+1)


dx = [1, -1]


def count_walls(mat, start):
    cnt = 0
    visited = set()
    q = collections.deque()
    q.append(start)
    while q:
        (i, j) = q.popleft()
        if (i, j) in visited:
            continue
        west = j - 1
        east = j + 1
        while mat[i][west] == '.':
            west -= 1
        while mat[i][east] == '.':
            east += 1
        cnt += 2

        for j in range(west+1, east):
            visited.add((i, j))
            for dx in (-1, 1):
                (ni, nj) = (i + dx, j)
                if (ni, nj) not in visited:
                    if mat[ni][nj] == '.':
                        q.append((ni, nj))
                    else:
                        cnt += 1

    for (i, j) in visited:
        mat[i][j] = cnt


# def count_walls(mat, start):
#     cnt = 0
#     visited = {start}
#     q = collections.deque()
#     q.append(start)
#     while q:
#         (i, j) = q.popleft()
#         for k in range(4):
#             ni = i + dx[k]
#             nj = j + dy[k]
#             if (ni, nj) not in visited:
#                 if mat[ni][nj] == '.':
#                     q.append((ni, nj))
#                     visited.add((ni, nj))
#                 else:
#                     cnt += 1
#     for (i, j) in visited:
#         mat[i][j] = cnt



def solve(mat, pairs):
    result = []
    for (x, y) in pairs:
        start = (i, j) = (x-1, y-1)
        if mat[i][j] == '.':
            count_walls(mat, start)
        result.append(mat[i][j])
    return result


def main():
    [n, m, k] = [int(c) for c in input().strip().split()]
    mat = [list(input().strip()) for _ in range(n)]
    positions = [tuple(int(c) for c in input().strip().split()) for _ in range(k)]
    assert len(mat[0]) == m
    assert len(positions[0]) == 2

    results = solve(mat, positions)
    for res in results:
        print(res)


if __name__ == '__main__':
    main()
