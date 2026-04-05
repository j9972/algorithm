import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [
    list(map(int,input().rstrip()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = []
cnt = 0

def possible(x,y):
    return 0<=x<n and 0<=y<n and not visited[x][y] and arr[x][y] == 1

def dfs(x,y):
    global cnt

    if possible(x,y):
        visited[x][y] = True
        cnt += 1

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            dfs(nx, ny)
        
        return True
    
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j):
            ans.append(cnt)
            cnt = 0

print(len(ans))
for i in sorted(ans):
    print(i)