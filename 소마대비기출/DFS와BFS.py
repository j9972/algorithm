# 실버 1 - 1260
from collections import deque
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())
visited1 = [[False] for _ in range(n+1)]
visited2 = [[False] for _ in range(n+1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
print(data)


def dfs(start):
    visited1[start] = True
    res = [start]

    for i in data[start]:
        if not visited1[i][1]:
            res.append(i)
            dfs(i)
    return res


# print(dfs(1))
