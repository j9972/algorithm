from collections import deque
import sys

n,k = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = [
    [sys.maxsize for _ in range(n)]
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

q = deque()
bad = []
time = 0
dxs,dys = [-1,1,0,0], [0,0,-1,1]

# 빈 공간은 -1로 상한 귤들은 0으로 
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            ans[i][j] = 0
            bad.append((i,j))
        if arr[i][j] == 0:
            ans[i][j] = -1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and arr[x][y] != 0 and not visited[x][y]

def push(x,y,val):
    q.append((x,y))
    visited[x][y] = True
    ans[x][y] = min(ans[x][y], val)

def init_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def bfs():
    global time

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy

            if can_go(nx,ny):
                push(nx,ny,ans[x][y]+1)

for i in bad:
    x,y = i

    init_visited()

    q.append((x,y))
    visited[x][y] = True

    bfs()

for i in range(n):
    for j in range(n):
        if ans[i][j] == sys.maxsize:
            ans[i][j] = -2

for i in ans:
    print(*i)