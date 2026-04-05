import sys
input = sys.stdin.readline

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

new_arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def possible(x,y):
    return 0<=x<n and 0<=y<m and arr[x][y] == 1 and not visited[x][y]

visited = [
    [False for _ in range(m)] 
    for _ in range(n)
]

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            visited[i][j] = True
            q.append((i,j))
            

while q:
    x,y = q.popleft()

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]

        if possible(nx,ny):
            visited[nx][ny] = True
            q.append((nx,ny))
            new_arr[nx][ny] = new_arr[x][y] + 1


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=' ')
        elif not visited[i][j]:
            print(-1, end=' ')
        else:
            print(new_arr[i][j],end=' ')
    print()