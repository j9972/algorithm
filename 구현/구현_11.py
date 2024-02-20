import copy
n = int(input())

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

arr_list = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def count_arround_pair(temp):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            visited[x][y] = True
            if temp[x][y] == 0:
                continue

            for dx, dy in zip(dxs, dys):
                nx,ny = x + dx, y + dy

                if not in_range(nx,ny) or visited[nx][ny]:
                    continue
                    
                if temp[x][y] == temp[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
    return cnt 

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

max_val = 0
for r in range(n):
    for c in range(n):

        temp = [[0] * n for _ in range(n)]
        arr = copy.deepcopy(arr_list) # 깊은 복사 ( 원본이 변경되지 않아 원본을 복사 )

        boom(r,c, arr[r][c])

        for i in range(n-1,-1,-1):
            for j in range(n):
                if arr[i][j] != 0:
                    for h in range(n-1,-1,-1):
                        if temp[h][j] == 0:
                            temp[h][j] = arr[i][j]
                            break

        max_val = max(max_val, count_arround_pair(temp))

print(max_val)