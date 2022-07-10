import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
    board.append(list(input()))

visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rgb = 0
gb = 0


def dfs(x, y):
    visited[x][y] = True
    color = board[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
            if color == board[nx][ny]:
                dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            rgb += 1
            dfs(i, j)

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            gb += 1
            dfs(i, j)
print(rgb, gb)
