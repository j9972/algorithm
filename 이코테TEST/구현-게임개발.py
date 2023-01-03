# 다시 다시 다시 다시 -,.-
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n)]
visited[x][y] = True


def turning():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


cnt = 1
turnCnt = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while True:
    turning()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if visited[nx][ny] == False and data[nx][ny] == 0:
        visited[nx][ny] = True
        x, y = nx, ny
        cnt += 1
        turnCnt = 0
        continue
    else:
        turnCnt += 1

    if turnCnt == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if data[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turnCnt = 0
print(cnt)
