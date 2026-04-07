import sys
input = sys.stdin.readline

n = int(input())

arr = [
    list(input().rstrip())
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

def possible(x,y):
    return 0<=x<n and 0<=y<n and not visited[x][y]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

dic = {}

def dfs(x,y):

    for dx, dy in zip(dxs,dys):
        nx,ny = x+dx, y+dy

        if possible(nx,ny) and arr[nx][ny] == arr[x][y]:
            visited[nx][ny] = True
            dfs(nx,ny)

normal = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            normal += 1
            dfs(i,j)

visited2 = [
    [False] * n
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

def possible2(x,y):
    return 0<=x<n and 0<=y<n and not visited2[x][y]

def dfs2(x,y):

    for dx, dy in zip(dxs,dys):
        nx,ny = x+dx, y+dy

        if possible2(nx,ny) and arr[nx][ny] == arr[x][y]:
            visited2[nx][ny] = True
            dfs2(nx,ny)
            
not_normal = 0

for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            not_normal += 1
            dfs2(i,j)

print(normal, not_normal)