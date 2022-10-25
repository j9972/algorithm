from collections import deque
from itertools import combinations
import sys
sys.setrecursionlimit(10**9)

n = int(input())

teacher = []
space = []
data = []

for i in range(n):
    data.append(list(map(str, input().split())))
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i, j))
        elif data[i][j] == 'X':
            space.append((i, j))


def watch(x, y, direction):
    # left -> right -> up -> down 순서
    if direction == 0:
        while y >= 0:
            if data[x][y] == 'T':
                return False
            elif data[x][y] == 'S':
                return True
            y -= 1
    if direction == 1:
        while y < n:
            if data[x][y] == 'T':
                return False
            elif data[x][y] == 'S':
                return True
            y += 1
    if direction == 2:
        while x >= 0:
            if data[x][y] == 'T':
                return False
            elif data[x][y] == 'S':
                return True
            x -= 1
    if direction == 3:
        while x < n:
            if data[x][y] == 'T':
                return False
            elif data[x][y] == 'S':
                return True
            x += 1
    return False


def process():
    for x, y in teacher:
        for i in range(4):
            if watch(x, y, i) == True:
                return True
    return False


find = True

for d in combinations(data, 3):
    for x, y in d:
        data[x][y] == 'O'

    if process():
        find = False
        break

    for x, y in d:
        data[x][y] = 'X'


if find == True:
    print('YES')
else:
    print('NO')
