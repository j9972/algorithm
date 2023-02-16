from itertools import combinations as cb
import sys
input = sys.stdin.readline

teacher = []
space = []
data = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
for i in range(n):
    data.append(list(map(str, input().split())))
for i in range(n):
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i, j))
        elif data[i][j] == 'X':
            space.append((i, j))


def watch(direction, x, y):  # 학생을 찾는 함수
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


def process():  # 찾았는지 확인
    for x, y in teacher:
        for i in range(4):
            if watch(i, x, y):
                return True
    return False


flag = True
for wall in cb(space, 3):
    for x, y in wall:
        data[x][y] = 'O'

    if process():
        flag = False
        break

    for x, y in wall:
        data[x][y] = 'X'


if flag:
    print('YES')
else:
    print('NO')
