# 3190 - 골드4
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

board = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
    x,y = map(int,input().split())
    board[x][y] = 1

l = int(input())
info = []
for i in range(l):
    t,c = map(str,input().split())
    info.append((int(t),c))

def turning(direction,c):
    if c == 'D':
        direction = (direction + 1 )% 4
    else:
        direction = (direction - 1 )% 4
    return direction 

def bfs():
    x,y = 1,1
    board[x][y] = 2
    direction = 0
    time = 1
    q = [(x,y)]
    cnt = 0

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1<=nx<=n and 1<=ny<=n and board[nx][ny] != 2:
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx,ny))

            elif board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx,ny))
                hx,hy = q.pop(0)
                board[hx][hy] = 0
        else:
            time += 1
            break
        time += 1
        x,y = nx,ny

        if time == info[cnt][0] and cnt < l:
            direction = turning(direction,info[cnt][1])
            cnt += 1
    return time

print(bfs())



