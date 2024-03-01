from collections import deque
n,h,m = map(int,input().split())

dxs, dys = [-1,1,0,0], [0,0,-1,1]

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

safety = [
    (i,j)
    for i in range(n)
    for j in range(n)
    if arr[i][j] == 3
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and arr[x][y] != 1

q = deque()

def push(nx,ny,new_temp):
    q.append((nx,ny))
    visited[nx][ny] = True
    temp[nx][ny] = new_temp

def bfs():

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx,ny = x + dx, y + dy

            if can_go(nx,ny):
                push(nx,ny, temp[x][y] + 1)

for x,y in safety:
    push(x,y,0)

bfs()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            if not visited[i][j]:
                print(-1,end=" ")
            else:
                print(temp[i][j],end=" ")
        else:  
            print(0,end=" ")
    print()