# 가로 세로
n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(str, input())))

count = []
resX = 0
resY = 0


def dfsX(x, y):
    if 0 <= x < n and 0 <= y < m and board[x][y] == '|':
        board[x][y] = '0'
        dfsX(x-1, y)
        dfsX(x+1, y)
        return True
    return False


def dfsY(x, y):
    if 0 <= x < n and 0 <= y < m and board[x][y] == '-':
        board[x][y] = '0'
        dfsY(x, y-1)
        dfsY(x, y+1)
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfsX(i, j) == True:
            resX += 1

for i in range(n):
    for j in range(m):
        if dfsY(i, j) == True:
            resY += 1


print(resX + resY)
