n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True

dxs,dys = [1,-1,0,0],[0,0,-1,1]

def dfs(x,y):
    global cnt
    
    for dx, dy in zip(dxs, dys):
        nx ,ny = x+ dx , y + dy

        if can_go(nx,ny):
            visited[nx][ny] = True
            cnt += 1
            dfs(nx,ny)

res = list()
for i in range(n):
    for j in range(n):
        if can_go(i,j):
            cnt = 1
            visited[i][j] = True
            dfs(i,j)
            res.append(cnt)

res.sort()
print(len(res))
for i in res:
    print(i)