from collections import deque

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs, dys = [-1,-1,-1,0,1,1,1,0], [-1,0,1,1,1,0,-1,-1]

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j))

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs():
    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy

            if not in_range(nx,ny):
                continue

            if arr[nx][ny] == 0:
                q.append((nx,ny))
                arr[nx][ny] = arr[x][y] + 1
    
bfs()
max_dist = 0
for i in range(n):
    for j in range(m):
        max_dist = max(max_dist, arr[i][j])
print(max_dist - 1)
