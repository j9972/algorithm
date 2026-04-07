import sys
input = sys.stdin.readline

y,x,z = map(int,input().split())

from collections import deque

arr = []

for _ in range(z):
    temp = []
    for _ in range(x):
        temp.append(list(map(int,input().split())))
    arr.append(temp)

# visited = []
# for _ in range(z):
#     temp_visited = [
#         [False] * y
#         for _ in range(x)
#     ]
#     visited.append(temp_visited)


dxs = [-1,1,0,0,0,0]
dys = [0,0,-1,1,0,0]
dzs = [0,0,0,0,-1,1]

def possible(a,b,c):
    return 0<=a<x and 0<=b<y and 0<=c<z and arr[c][a][b] == 0

q = deque()

def bfs():
    while q:
        z,x,y = q.popleft()

        for dx,dy,dz in zip(dxs,dys,dzs):
            nx = x + dx
            ny = y + dy
            nz = z + dz

            if possible(nx,ny,nz):
                arr[nz][nx][ny] = arr[z][x][y] + 1
                q.append((nz,nx,ny))

for h in range(z):
    for n in range(x):
        for m in range(y):
            if arr[h][n][m] == 1:
                q.append((h,n,m))

bfs()
days = -1
flag = False

for h in range(z):
    for n in range(x):
        for m in range(y):
            if arr[h][n][m] == 0:
                flag = True
            days = max(days, arr[h][n][m])

if flag:
    print(-1)
elif days == -1:
    print(0)
else:
    print(days-1)

