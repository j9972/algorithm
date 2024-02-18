# 시계, 반시계 어렵게 하지 말기

n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

tmp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

x, y, m1, m2, m3, m4, move_dir = tuple(map(int, input().split()))

def shift(x,y,k,l,d):
    if d == 0:
        dxs,dys = [-1,-1,1,1],[1,-1,-1,1]
        move_num = [k,l,k,l]
    else:
        dxs,dys = [-1,-1,1,1],[-1,1,1,-1]
        move_num = [l,k,l,k]
    
    for i in range(n):
        for j in range(n):
            tmp[i][j] = arr[i][j]
    
    for dx, dy, move in zip(dxs, dys, move_num):
        for _ in range(move):
            nx,ny = x + dx, y + dy
            tmp[nx][ny] = arr[x][y]
            x,y = nx,ny

    for i in range(n):
        for j in range(n):
            arr[i][j] = tmp[i][j]

shift(x-1, y-1, m1, m2, move_dir)

for i in arr:
    print(*i)