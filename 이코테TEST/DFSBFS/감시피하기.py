import sys
input = sys.stdin.readline
from itertools import combinations as cb

teacher = []
space = []
data = []
n = int(input())

for i in range(n):
    data.append(list(map(str, input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i,j))
        elif data[i][j] == 'X':
            space.append((i,j))

def watch(x,y,direction):
    # left
    if direction == 0:
        while y >= 0:
            if data[x][y] == 'S':
                return True
            elif data[x][y] == 'O':
                return False
            y -= 1
    # left
    if direction == 1:
        while y < n:
            if data[x][y] == 'S':
                return True
            elif data[x][y] == 'O':
                return False
            y += 1
    # left
    if direction == 2:
        while x >= 0:
            if data[x][y] == 'S':
                return True
            elif data[x][y] == 'O':
                return False
            x -= 1
    # left
    if direction == 3:
        while x < n:
            if data[x][y] == 'S':
                return True
            elif data[x][y] == 'O':
                return False
            x += 1
    return False


def process():
    for x,y in teacher:
        for i in range(4):
            if watch(x,y,i):
                return True# 찾았다
        return False  

flag = False
for wall in cb(teacher,3):
    for x,y in wall:
        data[x][y] = 'O'
    
    if not process():
        flag = True
        break

    for x,y in wall:
        data[x][y] = 'X'

if flag:
    print('YES')
else:
    print('NO')