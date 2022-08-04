from collections import deque

n, k = map(int, input().split())

board = []
data = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            data.append((board[i][j], 0, i, j))

data.sort()
queue = deque((data))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

target_s, target_x, target_y = map(int, input().split())

while queue:
    virus, s, x, y = queue.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))

print(board[target_x-1][target_y-1])
