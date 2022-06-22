from collections import deque

n, k = map(int, input().split())

g = []
d = []

for i in range(n):
    g.append(list(map(int, input().split())))
    for j in range(n):
        if g[i][j] != 0:
            d.append((g[i][j], 0, i, j))

tarS, tarX, tarY = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

d.sort()
queue = deque(d)

while queue:
    virus, s, x, y = queue.popleft()
    if s == tarS:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if g[nx][ny] == 0:
                g[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))
print(g[tarX-1][tarY-1])
