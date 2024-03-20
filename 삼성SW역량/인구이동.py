import sys
from collections import deque

n,L,R = map(int,input().split())

tot_days = 0

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def init_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def can_go(x,y):
    return in_range(x,y) and not visited[x][y]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    united = []
    united.append((x,y))

    population = arr[x][y]
    visited[x][y] = True

    for dx,dy in zip(dxs,dys):
        nx,ny = x + dx, y + dy

        if can_go(nx,ny):
            if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                population += arr[nx][ny]
                visited[nx][ny] = True
                q.append((nx,ny))
                united.append((nx,ny))
    
    for x,y in united:
        arr[x][y] = population // len(united)

while True:
    init_visited()

    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += 1
                bfs(i,j)
    
    if cnt == n**2:
        break
    tot_days += 1

print(tot_days)