import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

board = [[0] * (n+1) for _ in range(n+1)]

for i in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

l = int(input())

info = []
for i in range(l):
    t, direction = input().split()
    info.append((int(t), direction))


def turning(direction, c):
    if c == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    return direction


def process():
    x, y = 1, 1  # 처음 뱀 위치
    board[x][y] = 2  # 뱀이 있는 의치
    time = 0  # 이동 시간
    direction = 0
    cnt = 0  # 회전횟수 체크를 위함

    q = [(x, y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))

            elif board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
        else:
            time += 1
            break
        time += 1
        x, y = nx, ny

        if cnt < l and info[cnt][0] == time:
            direction = turning(direction, info[cnt][1])
            cnt += 1
    return time


print(process())
