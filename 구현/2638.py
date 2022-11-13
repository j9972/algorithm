from collections import deque
import sys
n, m = map(int, input().split())

cheese = []
for i in range(n):
    cheese.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if cheese[nx][ny] >= 1:
                    cheese[nx][ny] += 1
                else:
                    visited[nx][ny] = True
                    queue.append([nx, ny])


time = 0
while True:
    visited = [[False] * m for _ in range(n)]
    bfs()
    flag = 0

    for i in range(n):
        for j in range(m):
            if cheese[i][j] >= 3:
                cheese[i][j] = 0
                flag = 1
            elif cheese[i][j] == 2:
                cheese[i][j] = 1

    if flag == 1:
        time += 1
    else:
        break
print(time)
