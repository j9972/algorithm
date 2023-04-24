import sys
input = sys.stdin.readline
from collections import deque

n,l,r = map(int,input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = []
for i in range(n):
    board.append(list(map(int,input().split())))

def process(x,y,index):
    united = []
    united.append((x,y))

    q = deque()
    q.append((x,y))

    cnt = 1
    summary = board[x][y]
    union[x][y] = index

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx= x + dx[i]
            ny= y + dy[i]

            if 0<= nx <n and 0<=ny<n and union[nx][ny] == -1:
                if l<=abs(board[nx][ny]) - abs(board[x][y]) <=r:
                    union[nx][ny] = index
                    summary += board[nx][ny]
                    cnt += 1
                    q.append((nx,ny))
                    united.append((nx,ny))
    for i,j in united:
        board[i][j] = summary // cnt

    return cnt

tot = 0
while True:
    index = 0
    union = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j,index)
                index += 1
    if index == n*n:
        break
    tot += 1
print(tot)