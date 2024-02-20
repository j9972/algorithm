from collections import deque

n,k = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 나중에 -1씩 하기
starts = [
    map(int,input().split())
    for i in range(k)
]   

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or arr[x][y]:
        return False
    return True

def bfs():
    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx,ny = x + dx , y + dy

            if can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))

q = deque()
for i in starts:
    x,y = i
    visited[x-1][y-1] = True
    q.append((x-1, y-1))
    bfs()

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            cnt += 1
print(cnt)