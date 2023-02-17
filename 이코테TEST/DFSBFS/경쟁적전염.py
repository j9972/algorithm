import sys
input = sys.stdin.readline
from collections import deque
n,k = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

data = []
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            data.append((board[i][j], 0, i, j))


tars,tarx,tary = map(int,input().split())

data.sort()
q = deque(data)

while q:
    virus, s,x,y = q.popleft()

    if s == tars:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
            board[nx][ny] = virus
            q.append((virus, s+1, nx,ny))
print(board[tarx-1][tary-1])


