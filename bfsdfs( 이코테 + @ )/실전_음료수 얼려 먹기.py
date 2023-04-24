import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if 0<=x<n and 0<=y<m:
        if board[x][y] == 0:
            board[x][y] = 2
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
    return False

res = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            res += 1
print(res)
