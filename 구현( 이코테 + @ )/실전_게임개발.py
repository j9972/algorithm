import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())

x,y,direction = map(int,input().split())

visited = [[False] * m for _ in range(n)]
visited[x][y] = True

def rotate():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

board = []
for i in range(n):
    board.append(list(map(int,input().split())))

turnCnt = 0 # 4번의 방향을 돌았는지 체크
cnt = 1 # 방문한 칸의 수
while True:
    
    rotate()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if board[nx][ny] == 0 and visited[nx][ny] == False:
        turnCnt = 0
        visited[nx][ny] = True
        cnt += 1
        x = nx
        y = ny
        continue
    else:
        turnCnt += 1
    
    if turnCnt == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if board[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turnCnt = 0
print(cnt)