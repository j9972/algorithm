from collections import deque

n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))
    return board[n-1][m-1]


print(bfs(0, 0))
