# 3184 실버1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(str,input().rstrip())))

wolf, sheep = 0,0
w,s = 0,0

visited = [[False] * m for _ in range(n)]

def dfs(x,y):
    global wolf, sheep
    if 0<=x<n and 0<=y<m and visited[x][y] == False:
        if board[x][y] != '#':
            visited[x][y] = True
            if board[x][y] == 'o':
                sheep += 1
            elif board[x][y] == 'v':
                wolf += 1
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            if sheep > wolf:
                s += sheep
            else:
                w += wolf
            sheep , wolf = 0,0
print(s,w)
            