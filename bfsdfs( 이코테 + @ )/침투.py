# 13565 실버 2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(int,input().rstrip())))

def dfs(x,y):
    if 0<=x<n and 0<=y<m and board[x][y] == 0:
        board[x][y] = 2
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

for j in range(m):
    if board[0][j] == 0:
        dfs(0,j)

flag = False
for j in range(m):
    if board[n-1][j] == 2:
        flag = True
        break

if flag == True:
    print('YES')
else:
    print('NO')
    