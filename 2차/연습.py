import sys
input = sys.stdin.readline

from collections import deque

m,n,h = map(int,input().split())

arr = []
for _ in range(h):
    temp = [
        list(map(int,input().split()))
        for _ in range(n)
    ]
    arr.append(temp)

dxs = [-1,1,0,0,0,0]
dys = [0,0,-1,1,0,0]
dzs = [0,0,0,0,-1,1]

q = deque()

def possible(x,y,z):
    return 0<=x<n and 0<=y<m and 0<=z<h and arr[z][x][y] == 0


def bfs():
    while q:
        x,y,z = q.popleft()

        for dx,dy,dz in zip(dxs, dys, dzs):
            nx = x + dx
            ny = y + dy
            nz = z + dz

            if possible(nx,ny,nz):
                q.append((nx,ny,nz))
                arr[nz][nx][ny] = arr[z][x][y] + 1

flag = False
def initCheck(arr):
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if arr[z][x][y] == 0:
                    flag = True

initCheck(arr)

for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 1:
                q.append((x,y,z))

bfs()
days = -1

def zeroCheck(arr):
    global days
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if arr[z][x][y] == 0:
                    return True
                days = max(days, arr[z][x][y])
                
    return False

if zeroCheck(arr) == True:
    print(-1)
elif flag:
    print(0)
else:
    print(days-1)