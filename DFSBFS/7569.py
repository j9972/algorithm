import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = deque()

# 3차원 bfs문제


def bfs():
    while queue:
        # 높이, x,y 순서
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                # 높이, x,y 순서
                if board[nz][nx][ny] == 0:
                    board[nz][nx][ny] = board[z][x][y]+1
                    queue.append((nz, nx, ny))


# 시작점
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                queue.append((i, j, k))
bfs()
# res가 -2인 이유는 -1은 토마토가 없기 떄문
result = -2

# 익지 못하는 상황이 오면 종료
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0:
                print(-1)
                break
            #
            result = max(result, board[i][j][k])
# 익은 토마토의 숫자가 0으로 시작하기 때문이다.
print(result-1)
