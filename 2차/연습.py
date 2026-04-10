import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

from collections import deque

n = int(input())
arr = [
    list(input().rstrip())
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n and not visited[x][y]

def dfs(x,y):
    for dx,dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx,ny) and arr[x][y] == arr[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny)

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            cnt += 1    
            dfs(i,j)


for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited2 = [
    [False] * n
    for _ in range(n)
]

def in_range2(x,y):
    return 0<=x<n and 0<=y<n and not visited2[x][y]

cnt2 = 0
def dfs2(x,y):
    for dx,dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range2(nx,ny) and arr[x][y] == arr[nx][ny]:
            visited2[nx][ny] = True
            dfs2(nx,ny)

cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            visited2[i][j] = True
            cnt2 += 1    
            dfs2(i,j)

print(cnt,cnt2)