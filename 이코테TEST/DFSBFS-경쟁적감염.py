from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())

board = []
data = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            data.append((board[i][j], 0, i, j))

tarS, tarX, tarY = map(int, input().split())

data.sort()
q = deque(data)

while q:
    virus, s, x, y = q.popleft()

    if s == tarS:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = virus
            q.append((virus, s+1, nx, ny))

print(board[tarX-1][tarY-1])
