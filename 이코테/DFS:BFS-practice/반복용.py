from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 1:
                    data[nx][ny] = data[x][y] + 1
                    q.append((nx, ny))
    return data[n-1][m-1]


print(bfs(0, 0))
