# 토마토가 익는 최소 일수 구하기 BFS 문제
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 가로 세로 순서 ( 원래대로 풀면 된다 ) 2 ~ 1000
m, n = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 1 익 0 안익 -1 없
queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))

bfs()

flag = False

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            flag = True
            break


if flag:
    print(-1)
else:
    print(max(map(max, board))-1)
