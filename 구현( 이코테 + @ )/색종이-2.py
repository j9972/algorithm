# 2567 실버 4
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

board = [[0]*100 for _ in range(100)]

n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    for a in range(x,x+10):
        for b in range(y,y+10):
            board[a][b] = 1
res = 0
def checking(x,y):
    global res
    cnt = 0
    if board[x][y] == 1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if board[nx][ny] == 1:
                cnt += 1
        if cnt == 3:
            res += 1
        elif cnt == 2:
            res += 2
    return res

for i in range(100):
    for j in range(100):
        checking(i,j)
print(res)