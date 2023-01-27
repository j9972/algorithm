from itertools import combinations as cb
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

teacher = []
space = []

n = int(input())
data = []
for i in range(n):
    data.append(list(input().split()))
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i, j))
        elif data[i][j] == 'X':
            space.append((i, j))

# 학생 찾기


def watch(direction, x, y):
    # left
    if direction == 0:
        while y >= 0:
            if data[x][y] == 'O':  # 이 부분 T가 아니라 O 다. 장애물에 걸리는지 체크하는 부분이다.
                return False
            if data[x][y] == 'S':
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


flag = False
for wall in cb(space, 3):
    for x, y in wall:
        data[x][y] = 'O'

    if not process():
        flag = True  # 들켰다는 의미
        break

    for x, y in wall:
        data[x][y] = 'X'

if flag:
    print('YES')
else:
    print('NO')
