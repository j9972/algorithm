import sys
input = sys.stdin.readline

from collections import deque

n,m = map(int,input().split())

arr = [
    list(input())
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            q.append((i,j))
            visited[i][j] = True

def possible(x,y):
    return 0<=x<n and 0<=y<m and arr[x][y] != 'X' and not visited[x][y]

ans = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    x,y = q.popleft()

    for i in range(4):
        nx,ny = x + dx[i] , y + dy[i]

        if possible(nx,ny):
            visited[nx][ny] = True
            q.append((nx,ny))
            if arr[nx][ny] == 'P':
                ans += 1

if ans != 0:
    print(ans)
else:
    print('TT')

