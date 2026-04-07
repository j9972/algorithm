import sys
input = sys.stdin.readline
from collections import deque

y,x = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(x)
]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

q = deque()

for i in range(x):
    for j in range(y):
        if arr[i][j] == 1:
            q.append((i,j))

def possible(a,b):
    return 0<=a<x and 0<=b<y and arr[a][b] == 0

def bfs():
    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx,ny = x +dx, y+ dy

            if possible(nx,ny):
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))

bfs()
flag = False
days = -2

for i in range(x):
    for j in range(y):
        if arr[i][j] == 0:
            flag = True
        days = max(days, arr[i][j])

if flag:
    print(-1)
elif days == -1:
    print(0)
else:
    print(days-1)