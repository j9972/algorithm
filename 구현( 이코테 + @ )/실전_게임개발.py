import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n,m = map(int,input().split())

x,y,direction = map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(int,input().split())))

visited = [[False] * m for _ in range(n)]
visited[x][y] = True
res = 1

turn = 0

def direct():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:
    direct()

    nx = x + dx[direction]
    ny = y + dy[direction]

    if visited[nx][ny] == False and board[nx][ny] == 0:
        visited[nx][ny] = True
        res += 1
        x,y = nx,ny
        turn = 0
        continue
    else:
        turn += 1
    
    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if board[nx][ny] == 0:
            x,y = nx,ny
        else:
            break
        turn = 0
print(res)
