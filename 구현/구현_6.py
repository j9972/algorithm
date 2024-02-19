n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

r,c = map(int,input().split())
r -= 1
c -= 1

tmp = [
    [0] * n
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def boom(x,y,boomCnt):
    global arr

    arr[x][y] = 0
    
    for dx,dy in zip(dxs, dys):
        cur_x, cur_y = x,y
        
        for i in range(boomCnt - 1):
            nx,ny = cur_x + dx, cur_y + dy

            if not in_range(nx,ny):
                continue

            arr[nx][ny] = 0
            cur_x,cur_y = nx,ny

boom(r,c,arr[r][c])

for i in range(n-1,-1,-1):
    for j in range(n):
        if arr[i][j] != 0:
            for h in range(n-1,-1,-1):
                if tmp[h][j] == 0:
                    tmp[h][j] = arr[i][j]
                    break
for i in tmp:
    print(*i)

            