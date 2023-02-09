import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, direction = map(int, input().split())


def turning():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]
visited[x][y] = True

res = 1
turn = 0
while True:
    turning()

    nx = x + dx[direction]
    ny = y + dy[direction]
    if visited[nx][ny] == False and data[nx][ny] == 0:
        visited[nx][ny] = True
        x, y = nx, ny
        res += 1
        continue
    else:
        turn += 1

    if turn == 4:
        nx = x - dx[direction]
        nx = x + dx[direction]

        if data[nx][ny] == 1:
            break
        else:
            x, y = nx, ny
        turn = 0
print(res)
