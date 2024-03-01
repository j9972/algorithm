# 조합으로 푸는 문제
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

min_dist = sys.maxsize

def init_temp_visited():
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0
            visited[i][j] = False

if k != 0:
    for wall in list(cb(walls,2)):
        init_temp_visited()

        for x,y in wall:
            arr[x][y] = 0
        
        push(s_x-1,s_y-1,0)
        bfs()

        if visited[e_x-1][e_y-1]:
            min_dist = min(min_dist, temp[e_x-1][e_y-1])

        for x,y in wall:
            arr[x][y] = 1
else:
    push(s_x-1,s_y-1,0)
    bfs()

    if visited[e_x-1][e_y-1]:
        min_dist = min(min_dist, temp[e_x-1][e_y-1])

if min_dist == sys.maxsize:
    print(-1)
else:
    print(min_dist)