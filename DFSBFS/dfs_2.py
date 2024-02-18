n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True

dxs,dys = [1,0],[0,1]

def dfs(x,y):

    if x == n - 1 and y == m - 1:
        return
    
    for dx, dy in zip(dxs, dys):
        nx ,ny = x+ dx , y + dy

        if can_go(nx,ny):
            visited[nx][ny] += 1
            dfs(nx,ny)

visited[0][0] = 1
dfs(0,0)
print(visited[n-1][m-1])