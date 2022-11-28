# 음료수 얼려먹기
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 1:
                    data[nx][ny] = data[x][y] + 1
                    queue.append((nx, ny))
    return data[n-1][m-1]


print(dfs(0, 0))
