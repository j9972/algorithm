import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

board = []
for i in range(n):
    board.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

INF = int(1e9)

now_x,now_y = 0,0
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            now_x,now_y = i,j
            board[now_x][now_y] = 0
size = 2
def bfs():
    dist = [[-1] * n for _ in range(n)]
    dist[now_x][now_y] = 0
    q = deque([(now_x,now_y)])

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                # 지나가는거에 대한 함수이므로 size랑 크기가 같아도 지나살 수 있다
                if dist[nx][ny] == -1 and board[nx][ny] <= size: 
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist

def find(dist):
    min_dist = INF
    x,y = 0,0

    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= board[i][j] < size:
                if min_dist > dist[i][j]:
                    min_dist = dist[i][j]
                    x,y = i,j
    
    if min_dist == INF:
        return None
    else:
        return x,y,min_dist

time = 0
cnt = 0

while True:
    value = find(bfs())
    if value == None:
        print(time)
        break
    else:
        now_x,now_y = value[0], value[1]
        time += value[2]

        board[now_x][now_y] = 0
        cnt += 1

        if cnt >= size:
            size += 1
            cnt = 0

