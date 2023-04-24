import sys
input = sys.stdin.readline
from itertools import combinations as cb

n = int(input())

teacher = []
space = []
board = []

for i in range(n):
    board.append(list(map(str, input().split())))
    for j in range(n):
        if board[i][j] == 'X':
            space.append((i,j))
        elif board[i][j] == 'T':
            teacher.append((i,j))

def watch(direction,x,y):
    # left
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    # left
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    # left
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    # left
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False
            
def process():
    for x,y in teacher:
        for i in range(4):
            if watch(i, x, y):
                return True
    return False

find = False
for wall in cb(space,3):
    for x, y in wall:
        board[x][y] = 'O'
    
    if not process():
        find = True
        break

    for x, y in wall:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')