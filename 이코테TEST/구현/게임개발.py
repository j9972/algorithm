import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

visited = [[False] * (m+1) for _ in range(n+1)]
visited[x][y] = True

cnt = 1
turn = 0


def turning():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


while True:
    turning()

    nx = x + dx[direction]
    ny = y + dy[direction]

    if board[nx][ny] == 0 and visited[nx][ny] == False:
        visited[nx][ny] = True
        x, y = nx, ny
        cnt += 1
        continue
    else:
        turn += 1

    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if board[nx][ny] != 1:
            x, y = nx, ny
        else:
            break
        turn = 0
print(cnt)
