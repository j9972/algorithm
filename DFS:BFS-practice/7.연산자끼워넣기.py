# dfs 문제
from itertools import combinations
from math import comb

n = int(input())

graph = []
teachers = []
spaces = []
for i in range(n):
    graph.append(list(map(input())))
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        elif graph[i][j] == 'X':
            spaces.append((i, j))


def watch(x, y, direction):
    # left
    if direction == 0:
        while y >= 0:
            if graph[i][j] == 'S':
                return True
            elif graph[i][j] == 'O':
                return False
            y -= 1

    # right
    if direction == 1:
        while y < n:
            if graph[i][j] == 'S':
                return True
            elif graph[i][j] == 'O':
                return False
            y += 1

    # up
    if direction == 2:
        while x >= 0:
            if graph[i][j] == 'S':
                return True
            elif graph[i][j] == 'O':
                return False
            x -= 1

    # down
    if direction == 3:
        while x < n:
            if graph[i][j] == 'S':
                return True
            elif graph[i][j] == 'O':
                return False
            x += 1
    return False


def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


find = False

for data in combinations(spaces, 3):
    for x, y in data:
        graph[x][y] = 'O'
    if not process():
        find = True
        break
    for x, y in data:
        graph[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
