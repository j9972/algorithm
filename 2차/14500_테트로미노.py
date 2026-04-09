import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

max_val = max(map(max, arr))
ans = 0

def possible(x,y):
    return 0<=x<n and 0<=y<m and not visited[x][y]

def dfs(x,y,idx,total):
    global ans

    if ans >= total + max_val * (3-idx):
        return
    
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for dxs, dys in zip(dx,dy):
            nx,ny = x + dxs, y + dys

            if possible(nx,ny):
                if idx == 1:
                    visited[nx][ny] = True
                    dfs(x,y,idx+1,total+arr[nx][ny])
                    visited[nx][ny] = False
        
                visited[nx][ny] = True
                dfs(nx,ny,idx+1,total+arr[nx][ny])
                visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i,j,0,arr[i][j])
            visited[i][j] = False
print(ans)