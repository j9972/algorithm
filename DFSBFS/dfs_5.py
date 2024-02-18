import sys
boom = 0
max_val = -sys.maxsize

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y,num):
    if not in_range(x,y):
        return False
    if visited[x][y] or arr[x][y] != num:
        return False
    return True

def dfs(x,y,num):
    global cnt, max_val

    for dx, dy in zip(dxs, dys):
        nx,ny = x + dx, y + dy

        if can_go(nx, ny, num):
            visited[nx][ny] = True
            cnt += 1
            dfs(nx,ny,num)
            
    max_val = max(cnt, max_val)



for i in range(n):
    for j in range(n):
        num = arr[i][j]
        if can_go(i,j,num):
            cnt = 1
            visited[i][j] = True
            dfs(i,j,num)
        
            if cnt >= 4:
                boom += 1

print(boom, max_val)