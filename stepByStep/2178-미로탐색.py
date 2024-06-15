from collections import deque

n, m = map(int, input().split())

arr = [
    list(map(int,input()))
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    return in_range(x,y) and arr[x][y] == 1

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy

            if can_go(nx,ny):
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))

    return arr[n-1][m-1]

print(bfs(0,0))