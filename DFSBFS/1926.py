# dfs는 재귀관련 에러가 남 (RecursionError)
from collections import deque
n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*m for _ in range(n)]

# 전체개수
num = 0


def bfs(x, y):
    global num
    # 각 넓이를 위한 개수
    cnt = 0

    if board[x][y] == 0:
        return -1

    num += 1
    cnt += 1
    visited[x][y] = True

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                board[nx][ny] = board[x][y] + 1
                cnt += 1
                queue.append((nx, ny))
    return cnt


count = []


for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == False:
            count.append(bfs(i, j))
print(num)
# 그림이 하나도 없는 경우는 0
print(max(count) if count else 0)
