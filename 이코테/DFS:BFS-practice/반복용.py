from collections import deque
from itertools import combinations as cb
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

data = []
teacher = []
space = []

for i in range(n):
    data.append(list(map(str, input().split())))
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i, j))
        elif data[i][j] == 'X':
            space.append((i, j))


def watch(direction, x, y):
    # left
    if direction == 0:
        while y >= 0:
            if data[x][y] == 'O':
                return False
            elif data[x][y] == 'S':
                return True
            y -= 1
    # right
    if direction == 1:
        while y < n:
            if data[x][y] == 'O':
                return False
            if data[x][y] == 'S':
                return True
            y += 1
    # up
    if direction == 2:
        while x >= 0:
            if data[x][y] == 'O':
                return False
            if data[x][y] == 'S':
                return True
            x -= 1
    # down
    if direction == 3:
        while x < n:
            if data[x][y] == 'O':
                return False
            if data[x][y] == 'S':
                return True
            x += 1
    return False


def process():
    for x, y in teacher:
        for i in range(4):
            if watch(i, x, y):
                return True
    return False


find = False
for wall in cb(space, 3):
    for x, y in wall:
        data[x][y] = 'O'

    if not process():
        find = True
        break

    for x, y in wall:
        data[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
