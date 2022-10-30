from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

yr = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if data[nx][ny] != 0:
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
                elif data[nx][ny] == 0:
                    counted[x][y] += 1


while True:
    visit = [[0]*m for _ in range(n)]
    counted = [[0]*m for _ in range(n)]  # 녹는 빙하

    dummy = 0

    for i in range(n):
        for j in range(m):
            if data[i][j] != 0 and visit[i][j] == 0:
                visit[i][j] = 1
                bfs(i, j)
                dummy += 1

    for i in range(n):
        for j in range(m):
            if data[i][j] >= counted[i][j]:
                data[i][j] -= counted[i][j]
            else:
                data[i][j] = 0

    if dummy >= 2:
        print(yr)
        break
    elif not dummy:
        print(0)
        break
    else:
        yr += 1
