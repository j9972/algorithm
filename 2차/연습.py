import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

new = [
    [0 for _ in range(m)]
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i,j))
            visited[i][j] = True
            break

def possible(x,y):
    return 0<=x<n and 0<=y<m and not visited[x][y] and arr[x][y]  == 1

while q:
    x,y = q.popleft()

    for dx, dy in zip(dxs, dys):
        nx,ny = x + dx, y + dy

        if possible(nx,ny):
            new[nx][ny] = new[x][y] + 1
            visited[nx][ny] = True
            q.append((nx,ny))


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=' ')
        elif not visited[i][j]:
            print(-1, end=' ')
        else:
            print(new[i][j], end=' ')
    print()
