import sys
from collections import deque

n,L,R = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 상 우 하 좌
dxs,dys = [-1,0,1,0], [0,1,0,-1]

tot_days = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(nx,ny):
    return in_range(nx,ny) and not visited[nx][ny]

def process(x,y):
    q = deque()
    q.append((x,y))

    united = []
    united.append((x,y))

    poplutaion = arr[x][y]
    visited[x][y] = True

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx,ny = x + dx, y +dy

            if can_go(nx,ny):
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    poplutaion += arr[nx][ny]
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    united.append((nx,ny))
            
    for x,y in united:
        arr[x][y] = poplutaion // len(united)


while True:
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    idx = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                idx += 1
                process(i,j)
    
    if idx == n**2:
        break
    tot_days += 1

print(tot_days)