import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y, direction = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))


def turing():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


visited = [[False] * m for _ in range(n)]
visited[x][y] = True

cnt = 1
turn = 0

while True:
    turing()

    nx = x + dx[direction]
    ny = y + dy[direction]

    if data[nx][ny] == 0 and visited[nx][ny] == False:
        visited[nx][ny] = True
        x, y = nx, ny
        cnt += 1
        turn = 0
        continue
    else:
        turn += 1

    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if data[nx][ny] == 0:
            x, y = nx, ny
            turn = 0
        else:
            break


print(cnt)
