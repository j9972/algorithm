# 뱀
import sys
input = sys.stdin.readline

n = int(input())
appleCount = int(input())  # K

data = [[0] * (n+1) for _ in range(n+1)]
for i in range(appleCount):
    x, y = map(int, input().split())
    data[x][y] = 1

state = []

moving = int(input())
for i in range(moving):
    time, direction = input().split()
    state.append((int(time), direction))

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rotate(d, c):
    if c == 'L':
        d = (d-1) % 4
    else:
        d = (d+1) % 4
    return d


def sol():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0

    q = [(x, y)]

    time = 0
    index = 0  # 회전을 하는 횟수

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)  # 지나갈 자리
                data[px][py] = 0  # 방금 지나온 자리
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        time += 1
        x, y = nx, ny

        if index < moving and state[index][0] == time:
            direction = rotate(direction, state[index][1])
            index += 1
    return time


print(sol())
