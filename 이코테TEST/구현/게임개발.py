import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
x,y,direction = map(int,input().split())

data = []
for i in range(n):
    data.append(list(map(int,input().split())))

visited = [[False]*(m+1) for _ in range(n+1)]

def turing():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

visited[x][y] = True

turnCnt = 0
cnt = 1

while True:
    turing()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0<=nx<n and 0<=ny<m and data[nx][ny] == 0 and visited[nx][ny] == False:
        visited[nx][ny] = True
        cnt += 1
        x,y = nx,ny
        turnCnt = 0
        continue
    else:
        turnCnt += 1
    
    
    if turnCnt == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if  0<=nx<n and 0<=ny<n and data[nx][ny] == 0:
            x,y = nx,ny
            turnCnt = 0
        else:
            break
    
print(cnt)