import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

board = []
graph = [[0] * m for _ in range(n)]
for i in range(n):
    board.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            graph[nx][ny] = 2
            virus(nx,ny)

def getScore():
    score = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                score += 1
    return score

res = 0
def bfs(count):
    global res
    if count == 3:
        for i in range(n):
            for j in range(m):
                graph[i][j] = board[i][j]

        for i in range(n):
            for j in range(m):
                if graph[i][j] == 2:
                    virus(i,j)
        res = max(res,getScore())
        return
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                count += 1
                bfs(count)
                count -= 1
                board[i][j] = 0

bfs(0)
print(res)

