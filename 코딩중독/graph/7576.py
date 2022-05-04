from collections import deque
import sys
input = sys.stdin.readline


# 가로 = m, 세로 = n 1000이하
m, n = map(int, input().split())
ans = 0

graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

# 왼 오 위 아래
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])


bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            break
    ans = max(ans, max(i))

print(ans - 1)
