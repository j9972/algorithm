# 토마토가 다 익는 최소 일수
# done
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# m이 가로 n이 세로
m, n = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주변이 익지 않은 토마토일때 번지게 허기
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))


# 시작점을 찾아서 queue에 넣어주기
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))

bfs()

# 익지 못하는 상황이 오면 종료
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(-1)
            break
# 질문!! -1을 하는 이유
# 가장 큰값 - 1 ( 1부터 시작을 하니까)
print(max(map(max, board)) - 1)
