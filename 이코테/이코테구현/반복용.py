# 게임 개발
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

# 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 90도 회전


def turn():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0

while True:
    turn()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if data[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        count += 1
        x, y = nx, ny
        turn_time = 0
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if data[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0

        else:
            break
print(count)
