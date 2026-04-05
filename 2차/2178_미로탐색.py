from collections import deque

n, m = map(int, input().split())

arr = [
    list(map(int,input()))
    for _ in range(n)
]

dx,dy = [-1,1,0,0], [0,0,-1,1]

last_n , last_m = n-1, m-1

def possible(x,y):
    return 0<=x<n and 0<=y<m and arr[x][y] == 1

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if possible(nx,ny):
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))

    return arr[last_n][last_m]

print(bfs(0,0))