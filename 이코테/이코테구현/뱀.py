import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0]*(n+1) for _ in range(n+1)]
info = []

# 아래 1을 넣는 과정을 다르게 표현
# k_list = []
# for _ in range(k):
#     x, y = map(int, input().split())
#     k_list.append([x, y])

# for i in range(len(k_list)):
#     data[k_list[i][0]][k_list[i][1]] = 1

for i in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

l = int(input())
for i in range(l):
    x, c = input().split()
    info.append((int(x), c))


# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turing(direction, c):
    if c == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction


def simulate():
    x, y = 1, 1
    board[x][y] = 2
    direction = 0

    time = 0
    index = 0

    q = [(x, y)]  # 뱀위치

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        time += 1
        x, y = nx, ny

        if index < l and info[index][0] == time:
            direction = turing(direction, info[index][1])
            index += 1
    return time


print(simulate())
