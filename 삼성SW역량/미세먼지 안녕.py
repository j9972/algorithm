import sys

n,m,t = map(int,input().split())

up,down = -1,-1

# 시계방향 
dxs,dys = [0,-1,0,1],[1,0,-1,0]
# 반시계방향
dxss,dyss = [0,1,0,-1],[1,0,-1,0]

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

tmp = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    if arr[i][0] == -1: 
        up = i
        down = i+1
        break

def init_tmp():
    for i in range(n):
        for j in range(m):
            tmp[i][j] = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def dirty_can_go(x,y):
    return in_range(x,y) and arr[x][y] != -1

def dirty_wind():
    init_tmp()

    for x in range(n):
        for y in range(m):
            if arr[x][y] == 0 or arr[x][y] == -1:
                continue

            dirty_cnt = 0

            for dx,dy in zip(dxs,dys):
                nx,ny = x + dx, y + dy

                if dirty_can_go(nx,ny):
                    tmp[nx][ny] += arr[x][y] // 5
                    dirty_cnt += 1 
            arr[x][y] -= (arr[x][y] // 5 * dirty_cnt)

    for x in range(n):
        for y in range(m):
            arr[x][y] += tmp[x][y]

def air_up():
    before, direct = 0,0
    x,y = up,0
    
    while True:
        nx,ny = x + dxs[direct],y + dys[direct]

        if x == up and y == 0:
            break

        if not in_range(nx,ny):
            direct += 1
            continue

        arr[x][y], before = before, arr[x][y]
        x,y = nx,ny

def air_down():
    before, direct = 0,0
    x,y = down,0
    
    while True:
        nx,ny = x + dxss[direct],y + dyss[direct]

        if x == down and y == 0:
            break

        if not in_range(nx,ny):
            direct += 1
            continue

        arr[x][y], before = before, arr[x][y]
        x,y = nx,ny


for _ in range(t):
    dirty_wind()
    air_up()
    air_down()

tot_dirty = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] >= 1:
            tot_dirty += arr[i][j]

print(tot_dirty)