import sys
sys.setrecursionlimit(10**9)

n,m,k = map(int,input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

for _ in range(k):
    x,y = map(int,input().split())
    arr[x-1][y-1] = 1

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    return in_range(x,y) and arr[x][y] == 1

max_size = 0

def dfs(x,y):
    global max_size

    if can_go(x,y):
        arr[x][y] = 0
        max_size += 1

        for dx,dy in zip(dxs,dys):
            nx,ny = x + dx, y + dy

            dfs(nx,ny)

        return True
    return False

_list = []

for i in range(n):
    for j in range(m):
        if dfs(i,j):
            _list.append(max_size)
            max_size = 0

print(max(_list))
