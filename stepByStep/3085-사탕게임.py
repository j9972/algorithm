n = int(input())

arr = [
    list(input())
    for _ in range(n)
]

dxs, dys = [-1,1,0,0],[0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def change(x,y, nx,ny):
    if not in_range(nx,ny):
        return False
    
    if arr[x][y] != arr[nx][ny]:
        return True
    return False

def calc():
    res = 0

    # 행
    for i in range(n):
        tmp = 1  
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                tmp += 1
                res = max(res, tmp)
            else:
                tmp = 1

    # 열
    for j in range(n):
        tmp = 1  
        for i in range(1, n):
            if arr[i][j] == arr[i-1][j]:
                tmp += 1
                res = max(res, tmp)
            else:
                tmp = 1

    return res


max_val = 0
for x in range(n):
    for y in range(n):
        for dx,dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy

            if not change(x,y, nx,ny):
                continue

            arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]

            max_val = max(max_val, calc())

            arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]

print(max_val)
