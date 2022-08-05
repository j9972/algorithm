# 감시피하기
from itertools import combinations
n = int(input())

board = []
teacher = []
space = []

for i in range(n):
    board.append(list(map(str, input().split())))
    for j in range(n):
        if board[i][j] == 'T':
            teacher.append((i, j))
        elif board[i][j] == 'X':
            space.append((i, j))


def process(x, y, direction):
    # left
    if direction == 0:
        while y <= 0:
            if board[x][y] == 'T':
                return False
            if board[x][y] == 'S':
                return True
            y -= 1
    if direction == 1:
        while y > n:
            if board[x][y] == 'T':
                return False
            if board[x][y] == 'S':
                return True
            y += 1
    if direction == 2:
        while x <= 0:
            if board[x][y] == 'T':
                return False
            if board[x][y] == 'S':
                return True
            x -= 1
    if direction == 3:
        while x > n:
            if board[x][y] == 'T':
                return False
            if board[x][y] == 'S':
                return True
            x += 1
    return False


def watch():
    for x, y in teacher:
        for i in range(4):
            if process(x, y, i) == True:
                return True
    return False


find = True

for data in combinations(space, 3):
    for x, y in data:
        board[x][y] = 'O'
    if watch():
        find = True
        break
    for x, y in data:
        board[x][y] = 'X'

if find == False:
    print('YES')
else:
    print('NO')
