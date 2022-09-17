from collections import deque

n, k = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = []
graph = []

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            graph.append((board[i][j], 0, i, j))

tarS, tarX, tarY = map(int, input().split())

graph.sort()
queue = deque(graph)

while queue:
    virus, s, x, y = queue.popleft()

    if s == tarS:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))

print(board[tarX-1][tarY-1])
