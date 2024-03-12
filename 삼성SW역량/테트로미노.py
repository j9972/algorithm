import sys

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = max(map(max, arr))

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dxs,dys = [-1,0,1,0],[0,1,0,-1]
ans = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    return in_range(x,y) and not visited[x][y]

def dfs(x,y,idx,total):
    global ans

    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nx,ny = x + dxs[i], y + dys[i]

            if can_go(nx,ny):
                if idx == 1:
                    visited[nx][ny] = True
                    dfs(x,y,idx+1, total + arr[nx][ny])
                    visited[nx][ny] = False

                visited[nx][ny] = True
                dfs(nx,ny,idx+1, total + arr[nx][ny])
                visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,0,arr[i][j])
        visited[i][j] = False

print(ans)