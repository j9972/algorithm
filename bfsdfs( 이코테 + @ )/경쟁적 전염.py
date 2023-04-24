import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().split())

data = []
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append([graph[i][j], 0, i,j])

data.sort()
q = deque(data)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

t_s,t_x,t_y = map(int,input().split())

while q:
    virus,s,x,y = q.popleft()
    if s == t_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                data.append([graph[nx][ny], s+1, nx,ny])
print(graph[t_x -1][t_y-1])