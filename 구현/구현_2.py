# 2차원 바람
n,m,q = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

wind = []
for i in range(q):
    x1,y1, x2,y2 = map(int,input().split())
    wind.append((x1-1, y1-1, x2-1, y2-1))

def shift(x1,y1,x2,y2):
    tmp = arr[x1][y1]

    for i in range(x1, x2):
        arr[i][y1] = arr[i + 1][y1]
    
    for i in range(y1, y2):
        arr[x2][i] = arr[x2][i + 1]
    
    for i in range(x2, x1 , -1):
        arr[i][y2] = arr[i - 1][y2]
    
    for i in range(y2, y1, -1):
        arr[x1][i] = arr[x1][i -1]
    
    arr[x1][y1 + 1] = tmp

dxs, dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def avgVal(arr,x,y):
    cur = arr[x][y]
    cnt = 1

    for dx, dy in zip(dxs, dys):
        nx , ny = x+dx, y +dy

        if not in_range(nx,ny):
            continue
    
        cur += arr[nx][ny]
        cnt += 1


    #print(cur, cnt, int(cur / cnt))
    return int(cur / cnt)

for i in wind:
    x1, y1, x2, y2 = i

    shift(x1, y1, x2, y2)

    shift_arr = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(m):
            shift_arr[i][j] = arr[i][j]
    
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            arr[i][j] = avgVal(shift_arr, i,j)

for i in arr:
    print(*i)