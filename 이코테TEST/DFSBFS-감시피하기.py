from itertools import combinations as cb
import sys
input = sys.stdin.readline

n = int(input())

space = []
teacher = []
data = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    data.append(list(map(str, input().split())))
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i, j))
        elif data[i][j] == 'X':
            space.append((i, j))


def watch(x, y, direction):
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
            elif data[x][y] == 'S':
                return True
            y += 1
    # up
    if direction == 2:
        while x >= 0:
            if data[x][y] == 'O':
                return False
            elif data[x][y] == 'S':
                return True
            x -= 1
    # down
    if direction == 3:
        while x < n:
            if data[x][y] == 'O':
                return False
            elif data[x][y] == 'S':
                return True
            x += 1
    return False


def check():
    for x, y in teacher:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


escape = False
for wall in cb(space, 3):
    for x, y in wall:
        data[x][y] = 'O'

    if not check():
        # 감시를 피하는게 목적임을 잊으면 안된다
        escape = True
        break

    for x, y in wall:
        data[x][y] = 'X'

if escape:
    print('YES')
else:
    print('NO')
