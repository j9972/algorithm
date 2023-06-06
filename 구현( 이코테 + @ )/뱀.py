import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
    r,c = map(int,input().split())
    board[r][c] = 1

l = int(input())
info = []
for i in range(l):
    x,c = input().split()
    info.append([int(x), c])

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction,c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def process():
    x,y = 1,1
    board[x][y] = 2
    time , index, direction = 0,0,0
    q = [(x,y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1<=nx<=n and 1<=ny<=n and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx,ny))
                hx,hy = q.pop(0)
                board[hx][hy] = 0
            elif board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx,ny))
        else:
            time += 1
            break
        time += 1
        x,y = nx,ny

        if index < l and time == info[index][0]:
            direction = turn(direction,info[index][1])
            index += 1
    return time
print(process())