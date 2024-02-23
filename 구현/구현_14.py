n = int(input())
x,y = map(int,input().split())

x -= 1
y -= 1
direct = 1

dx , dy = [-1,0,1,0], [0,1,0,-1]

arr = []
for i in range(n):
    tmp = list()
    for i in list(input()):
        if i == '.':
            tmp.append(1)
        else:
            tmp.append(0)
    arr.append(tmp)

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    nx,ny = x + dx[direct] , y + dy[direct]

    if not in_range(nx,ny):
        return True
    return arr[nx][ny]

def empty(x,y):
    nx,ny = x + dx[(direct + 1) % 4] , y + dy[(direct + 1) % 4]

    if not in_range(nx,ny):
        return True
    return arr[nx][ny]

def move():
    global x,y,direct

    turningCnt,time = 0,0

    while True:
        if not in_range(x,y):
            return time
        
        elif can_go(x,y):
            x,y = x + dx[direct], y + dy[direct]
            turningCnt = 0
            time += 1

            if empty(x,y): # 전진했는데 바닥에 없으면 시계방향으로 회정
                direct = (direct + 1) % 4
        
        elif not can_go(x,y):
            turningCnt += 1
            direct = (direct + 3) % 4 # 갈수없으면 반시계 방향으로 회전
        
        if turningCnt == 4 or time >= n * n:
            return -1

ans = move()
print(ans)