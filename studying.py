# 뿌요 뿌요
from collections import deque
import sys
input = sys.stdin.readline

data = []
for _ in range(12):
    data.append(list(input().rstrip()))
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque([(x, y)])
    pos = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] == False:
                if data[nx][ny] == data[x][y]:
                    pos.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = True
    if len(pos) >= 4:
        pos.sort(key=lambda x: (x[1], x[0]))
        for i, j in pos:
            data[i][j] = '_'
            bomb.append([i, j])


while True:
    visited = [[False] * 6 for _ in range(12)]
    bomb = []

    for i in range(12):
        for j in range(6):
            if data[i][j] != '.' and data[i][j] != '_' and visited[i][j] == False:
                bfs(i, j)

    if len(bomb) == 0:
        break

    for b in bomb:
        x, y = b[0], b[1]
        for i in range(x, 0, -1):
            data[i][y] = data[i-1][y]
        data[0][y] = '.'
    cnt += 1
print(cnt)
