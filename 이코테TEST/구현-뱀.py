import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0]*(n+1) for _ in range(n+1)]  # (1,1) 이 시작

for i in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

changingCount = int(input())
info = []
for i in range(changingCount):
    x, c = map(str, input().split())
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turning(direction, c):
    if c == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction


x, y = 1, 1
q = [(x, y)]
board[x][y] = 2
direction = 0
time = 0
cnt = 0

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            q.append((nx, ny))
            px, py = q.pop(0)
            board[px][py] = 0
        elif board[nx][ny] == 1:
            board[nx][ny] = 2
            q.append((nx, ny))
    else:
        time += 1
        break
    time += 1
    x, y = nx, ny

    if cnt < changingCount and info[cnt][0] == time:
        direction = turning(direction, info[cnt][1])
        cnt += 1
print(time)
