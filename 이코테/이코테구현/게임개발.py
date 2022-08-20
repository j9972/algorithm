import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

d = [[False] * m for _ in range(n)]
d[x][y] = True
res = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

turn = 0


def turning():
    global direction
    # 계속 한바퀴씩 돌려야하는데
    direction -= 1
    if direction == -1:
        direction = 3


while True:
    turning()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == False and board[nx][ny] == 0:
        board[nx][ny] = 1
        x = nx
        y = ny
        res += 1
        turn = 0

    else:
        turn += 1

    if turn == 4:
        # 뒤로 갈 수 있으면 가기
        nx = x - dx[direction]
        ny = y - dy[direction]

        if board[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0
print(res)
