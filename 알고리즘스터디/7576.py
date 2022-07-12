# 토마토가 다 익는 최소 일수
# keep
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# m이 가로 n이 세로
m, n = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

flag = False


def bfs():
    global flag
    queue = deque()
    count = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (board[nx-1][ny] == -1 or board[nx-1][ny] == 0) and (board[nx+1][ny] == -1 or board[nx+1][ny] == n) and (board[nx][ny-1] == -1 or board[nx][ny-1] == 0) and (board[nx][ny+1] == -1 or board[nx][ny+1] == m):
                print(-1)
                break

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    board[nx][ny] = board[x][y] + 1
                    count += 1
                    queue.append((nx, ny))
                    flag = True
        return count


# 처음부터 익을 수 없는경우
for _ in range(n):
    for _ in range(m):
        if 0 not in board and 1 not in board:
            print(0)
            break
bfs()
