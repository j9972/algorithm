n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dxs, dys = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

def move(x,y):
    max_x, max_y, max_val = -1,-1,0

    for dx,dy in zip(dxs, dys):
        nx,ny = x + dx, y + dy

        if not in_range(nx,ny):
            continue

        if arr[nx][ny] > max_val:
            max_val = arr[nx][ny]
            max_x, max_y = nx,ny
    
    arr[max_x][max_y] = arr[x][y]
    arr[x][y] = max_val

def move_all():
    idx = 1
    while idx <= n ** 2:
        for i in range(n):
            for j in range(n):
                if arr[i][j] == idx:
                    move(i,j)
                    idx += 1
                else:
                    continue


for _ in range(m):
    move_all()

for i in arr:
    print(*i)