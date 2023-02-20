# 실버1 - 2583
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m,k = map(int,input().split())

board = [[0] * m for _ in range(n)]

for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            if board[y][x] == 0:
                board[y][x] = 1


ans = 0
def dfs(x,y):
    global ans
    if 0<=x<n and 0<=y<m:
        if board[x][y] == 0:
            board[x][y] = 1
            ans += 1
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
    return False

res = 0
l = []
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            l.append(ans)
            ans = 0
            res += 1
print(res)
l.sort()
for i in l:
    print(i, end=' ')



