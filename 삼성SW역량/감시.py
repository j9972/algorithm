import sys
from itertools import product

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(m)]
    for _ in range(n)
]

min_val = n * m

cctv = []
for i in range(n):
    for j in range(m):
        if arr[i][j] in [1,2,3,4,5]:
            cctv.append((i,j,arr[i][j]))

dxs,dys = [0,1,0,-1],[1,0,-1,0]

cctv_direction = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def init_temp():
    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[i][j]

def getSize():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt

tmp = list()
for _, _, val in cctv:
    tmp.append(cctv_direction[val])

for prod in list(product(*tmp)):
    init_temp()

    for i in range(len(cctv)):
        for d in prod[i]:
            x,y,_ = cctv[i][0],cctv[i][1],cctv[i][2]

            while True:
                nx,ny = x + dxs[d],y + dys[d]

                if not in_range(nx,ny):
                    break
                if temp[nx][ny] == 6:
                    break
                elif temp[nx][ny] == 0:
                    temp[nx][ny] = -1

                x,y = nx,ny
            
    min_val = min(min_val, getSize())

print(min_val)