#14716 실버1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(int,input().split())))

def dfs(x,y):
    if 0<=x<n and 0<=y<m and board[x][y] == 1:
        board[x][y] = 2
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y-1)
        dfs(x-1,y+1)
        dfs(x+1,y-1)
        dfs(x+1,y+1)
        return True
    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            cnt += 1
print(cnt)