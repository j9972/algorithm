from collections import deque

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dxs, dys = [-1,1,0,0], [0,0,-1,1]

q = deque()
q.append((0,0))

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True

def bfs():
    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy

            if can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))

bfs()

if visited[n-1][m-1]:
    print(1)
else:
    print(0)
            