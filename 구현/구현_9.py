n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

boooooooo = [
    int(input())
    for _ in range(m)
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

for i in boooooooo:
    col = i
    col -= 1

    tmp = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for j in range(n):
        if arr[j][col] != 0:
            boom(j,col,arr[j][col])
            break
        else:
            continue
    
    # print('--------------check')
    # for i in arr:
    #     print(*i)

    for i in range(n-1,-1,-1):
        for j in range(n):
            if arr[i][j] != 0:
                for h in range(n-1,-1,-1):
                    if tmp[h][j] == 0:
                        tmp[h][j] = arr[i][j]
                        break

    for i in range(n):
        for j in range(n):
            arr[i][j] = tmp[i][j]
for i in arr:
    print(*i)
