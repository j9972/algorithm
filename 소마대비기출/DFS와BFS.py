# 실버 1 - 1260
from collections import deque
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data = [[] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)


def dfs(start):
    visited1[start] = True
    print(start, end=' ')

    for i in data[start]:
        if not visited1[i]:
            dfs(i)


def bfs(start):
    q = deque([start])
    visited2[start] = True

    while q:
        now = q.popleft()

        print(now, end=' ')

        for i in data[now]:
            if not visited2[i]:
                visited2[i] = True
                q.append(i)


for i in range(n):
    data[i].sort()

dfs(start)
print()
bfs(start)
