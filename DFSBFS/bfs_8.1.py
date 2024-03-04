from collections import deque
from itertools import combinations as cb
import sys

n,k,u,d = map(int,input().split())
max_val = -sys.maxsize

dxs,dys = [-1,1,0,0], [0,0,-1,1]

ans = 0
q = deque()

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

coords_list = []
coords = [
    (i,j)
    for i in range(n)
    for j in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(nx,ny,height):
    return in_range(nx,ny) and u <= abs(arr[nx][ny] - height) <= d and not visited[nx][ny]
    
def push(nx,ny):
    visited[nx][ny] = True
    q.append((nx,ny))

def init_visited():
    global visited 

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def bfs():
    
    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy

            if can_go(nx,ny,arr[x][y]):
                push(nx,ny)

def calc():
    init_visited()

    for x,y in coords_list:
        q.append((x,y))
        visited[x][y] = True
    
    bfs()

    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
    return cnt

def choose(idx, cnt):
    global ans

    if cnt > k:
        return
    
    if idx == n ** 2:
        if cnt == k:
            ans = max(ans, calc())
        return
    
    coords_list.append(coords[idx])
    choose(idx+1, cnt+1)
    coords_list.pop()
    choose(idx+1, cnt)

choose(0,0)
print(ans)