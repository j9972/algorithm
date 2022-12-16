# 뿌요 뿌요
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    pos = []
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] == False:
                if data[x][y] == data[nx][ny]:
                    q.append((nx, ny))
                    pos.append((nx, ny))
                    visited[nx][ny] = True
    if len(pos) >= 4:
        pos.sort(key=lambda x: (x[1], x[0]))
        for i, j in pos:
            data[i][j] = '_'
            bomb.append([i, j])


data = []
for _ in range(12):
    data.append(list(input().rstrip()))
cnt = 0

while True:

    bomb = []
    visited = [[False] * 6 for _ in range(12)]

    for x in range(12):
        for y in range(6):
            if data[x][y] != '.' and data[x][y] != '_' and visited[x][y] == False:
                bfs(x, y)

    if len(bomb) == 0:
        break

# 한칸씩 내리기 ( row를 생각해야함 )
    for b in bomb:
        x, y = b[0], b[1]
        for i in range(x, 0, -1):
            data[i][y] = data[i-1][y]
        data[0][y] = '.'

    cnt += 1

print(cnt)
