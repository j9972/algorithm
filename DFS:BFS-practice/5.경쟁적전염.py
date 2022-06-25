from collections import deque

n, k = map(int, input().split())

data = []
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

tarS, tarX, tarY = map(int, input().split())

data.sort()
queue = deque(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    virus, s, x, y = queue.popleft()
    if s == tarS:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))
print(graph[tarX-1][tarY-1])
