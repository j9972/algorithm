import sys
input = sys.stdin.readline

n, m = map(int, input().split())

x, y, direction = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

data = []
for i in range(n):
    data.append(list(map(int, input().split())))


def turning():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


cnt = 1
turningCnt = 0
data[x][y] = 2

while True:
    turning()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
        data[nx][ny] = 2
        x = nx
        y = ny
        turningCnt = 0
        cnt += 1
    else:
        turningCnt += 1

    if turningCnt == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if data[nx][ny] == 2:
            x = nx
            y = ny
            turningCnt = 0
        else:
            break
print(cnt)
