from itertools import combinations

n = int(input())
board = []  # 전체
teacher = []
space = []  # 빈공간

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teacher.append((i, j))
        if board[i][j] == 'X':
            space.append((i, j))


def watch(x, y, direction):
    # left
    if direction == 0:
        while y >= 0:
            if board[i][j] == 'S':
                return True
            if board[i][j] == 'O':
                return False
            y -= 1
    # right
    if direction == 1:
        while y < n:
            if board[i][j] == 'S':
                return True
            if board[i][j] == 'O':
                return False
            y += 1
    # up
    if direction == 2:
        while x >= 0:
            if board[i][j] == 'S':
                return True
            if board[i][j] == 'O':
                return False
            x -= 1
    # down
    if direction == 3:
        while x < n:
            if board[i][j] == 'S':
                return True
            if board[i][j] == 'O':
                return False
            x += 1
    return False


def process():
    for x, y in teacher:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


find = False

for data in combinations(space, 3):
    for x, y in data:
        board[x][y] == 'O'
    if not process():
        find = True
        break
    for x, y in data:
        board[x][y] == 'X'

if find:
    print('YES')
else:
    print('NO')
