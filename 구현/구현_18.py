n,m,t = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

next_arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

tmp = [
    [0 for _ in range(n)]
    for _ in range(n)
]      

for _ in range(m):
    x,y = map(int,input().split())
    next_arr[x-1][y-1] = 1

dxs,dys = [-1,1,0,0],[0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def get_next_pos(x,y):
    max_x, max_y = x, y
    max_val = 0

    for dx,dy in zip(dxs, dys):
        nx,ny = x + dx, y + dy

        if not in_range(nx,ny):
            continue

        # 동일한 값들에 대해서는 먼저 나오는게 우선순위를 가져서 이렇게 하기
        if arr[nx][ny] > max_val: 
            max_val = arr[nx][ny]
            max_x, max_y = nx, ny

    return max_x, max_y

def move(x,y):
    nx,ny = get_next_pos(x,y)

    tmp[nx][ny] += 1

def move_all():
    for i in range(n):
        for j in range(n):
            tmp[i][j] = 0

    for i in range(n):
        for j in range(n):
            if next_arr[i][j]:
                move(i,j)

    for i in range(n):
        for j in range(n):
            if tmp[i][j] >= 2:
                tmp[i][j] = 0
            next_arr[i][j] = tmp[i][j]

for _ in range(t):
    move_all()
    
val = 0
for i in range(n):
    for j in range(n):
        if next_arr[i][j]:
            val += 1
print(val)