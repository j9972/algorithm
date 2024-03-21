import sys
from collections import deque

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

cnt ,time, size = 0, 0, 2 

dxs,dys =[-1,0,1,0], [0,-1,0,1]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

cur_x, cur_y = 0,0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            cur_x, cur_y = i,j

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def init_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def can_go(x,y):
    return in_range(x,y) and arr[x][y] <= size and not visited[x][y]

def can_eat(x,y):
    return arr[x][y] != 0 and arr[x][y] < size

def bfs():
    global cur_x, cur_y, size

    dist = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    init_visited()

    q = deque()
    q.append((cur_x, cur_y))

    visited[cur_x][cur_y] = True
    eat_fishes = []

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs, dys):
            nx,ny = x +dx , y +dy

            if can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1

                if can_eat(nx,ny):
                    eat_fishes.append((nx,ny, dist[nx][ny]))

    return sorted(eat_fishes, key=lambda x : (-x[2],-x[0],-x[1]))

while True:
    ate_fishes = bfs()

    if len(ate_fishes) == 0:
        break

    next_x,next_y,distance = ate_fishes.pop()

    time += distance
    arr[next_x][next_y] = 0

    cur_x,cur_y = next_x,next_y
    cnt += 1
    
    if cnt >= size:
        size += 1
        cnt = 0

print(time)