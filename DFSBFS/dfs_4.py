import sys
n,m = map(int,input().split())
sys.setrecursionlimit(10**5)

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y,k):
    if not in_range(x,y):
        return False
    if visited[x][y] or arr[x][y] <= k:
        return False
    return True

dxs, dys = [-1,1,0,0], [0,0,-1,1]

def dfs(x,y,k):
    for dx, dy in zip(dxs, dys):
        nx,ny = x+dx, y+dy

        if can_go(nx,ny,k):
            visited[nx][ny] = True
            dfs(nx,ny,k)

ans = list()
for k in range(1,101):
    res = 0

    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(m):
            if can_go(i,j,k):
                res += 1
                visited[i][j] = True
                dfs(i,j,k)

    ans.append((res,k))

ans.sort(key = lambda x : (-x[0], x[1]))

print(ans[0][1], ans[0][0])