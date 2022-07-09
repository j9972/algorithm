# 도움 받음

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 ( 대각선은 안됨 )
from collections import deque

# 가로 세로 순서 ( 원래대로 풀면 된다 ) 2 ~ 1000
m, n, h = map(int, input().split())
board = []
queue = deque()

# 높이에 대한 변수가 가장 먼저 나와야한다.
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(h):
    for j in range(n):
        board.append(list(map(int, input().split())))


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and board[nz][nx][ny] == 0:
                board[nz][nx][ny] = board[z][x][y] + 1
                queue.append((nz, nx, ny))


for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                queue.append((i, j, k))

bfs()

z = 1
res = -1

for i in board:
    for j in i:
        for k in j:
            if k == 0:
                z = 0

            res = max(res, k)

if z == 0:
    print(-1)
elif res == 1:
    print(0)
else:
    print(res-1)
