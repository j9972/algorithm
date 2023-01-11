from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False]*(m+1) for _ in range(n+1)]
visited[x][y] = True


def turning():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


data = []
for i in range(n):
    data.append(list(map(int, input().split())))

cnt = 1
turningPoint = 0
while True:
    turning()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if data[nx][ny] == 0 and visited[nx][ny] == False:
        data[nx][ny] = 1
        visited[nx][ny] = True
        cnt += 1
        turningPoint = 0
        x, y = nx, ny
    else:
        turningPoint += 1

    if turningPoint == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if data[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turningPoint = 0
print(cnt)
