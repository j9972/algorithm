# 왕실의 나이트
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 방문 처리
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


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
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있나?
        if data[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(count)
