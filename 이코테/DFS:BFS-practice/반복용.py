from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

s, x, y = map(int, input().split())

while q:
    v, ts, tx, ty = q.popleft()

    if s == ts:
        break
    for i in range(4):
        nx = tx + dx[i]
        ny = ty + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                q.append((v, ts+1, nx, ny))

print(graph[x-1][y-1])
