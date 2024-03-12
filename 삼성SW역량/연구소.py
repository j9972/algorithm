import sys

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(m)]
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def getSize():
    size = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                size+=1
    return size

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    return in_range(x,y) and temp[x][y] == 0

def virus_spread(x,y):
    for dx,dy in zip(dxs, dys):
        nx,ny = x + dx, y + dy

        if can_go(nx,ny):
            temp[nx][ny] = 2
            virus_spread(nx,ny)

def calc():
    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[i][j]

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                virus_spread(i,j)
    return getSize()

res = 0
def dfs(cnt):
    global res

    if cnt == 3:
        res = max(res, calc())
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1

                dfs(cnt)

                cnt -= 1
                arr[i][j] = 0

dfs(0)
print(res)
