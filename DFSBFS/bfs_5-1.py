# 백트래킹으로 푸는 bfs문제
from itertools import combinations as cb
from collections import deque
import sys

n,k = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

walls = [
    (i,j)
    for i in range(n)
    for j in range(n)
    if arr[i][j]
]

s_x, s_y = map(int,input().split())
e_x, e_y = map(int,input().split())
dxs,dys = [-1,1,0,0], [0,0,-1,1]

def push(nx,ny,new_temp):
    visited[nx][ny]= True
    q.append((nx,ny))
    temp[nx][ny] = new_temp

q = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and arr[x][y] != 1 and not visited[x][y]

def bfs():

    while q:
        x,y = q.popleft()
        
        for dx,dy in zip(dxs,dys):
            nx,ny = x + dx, y + dy

            if can_go(nx,ny):
                push(nx,ny,temp[x][y] + 1)
    
    if visited[e_x-1][e_y-1]:
        return temp[e_x-1][e_y-1]
    else:
        return sys.maxsize

min_dist = sys.maxsize

def init_temp_visited():
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0
            visited[i][j] = False

def find(idx, cnt):
    global min_dist

    if idx == len(walls):
        if cnt == k:
            init_temp_visited()

            push(s_x-1, s_y-1, 0)
            ans = bfs()
            min_dist = min(min_dist, ans)

        return
    
    x,y = walls[idx]
    arr[x][y] = 0
    find(idx+1, cnt+1)
    arr[x][y] = 1
    find(idx+1, cnt)
find(0,0)    


if min_dist == sys.maxsize:
    min_dist = -1

print(min_dist)