import sys
import copy

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

maps = []

# 동 남 서 북 ( 시계 방향 )
dxs,dys = [0,1,0,-1],[1,0,-1,0]

min_val = n * m
cctv_cnt = 0
cctv = []

cctv_direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [1, 0, 3]],
    [[0, 1, 2, 3]]
]

for i in range(n):
    data = list(map(int, input().split()))
    maps.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append((i,j,data[j]))
            cctv_cnt += 1

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def getSize():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                cnt += 1
    return cnt

def watching(maps, direct, x, y):
    
    for d in direct:
        cur_x, cur_y = x, y

        while True:
            nx,ny = cur_x + dxs[d], cur_y + dys[d]

            if not in_range(nx,ny):
                break

            if maps[nx][ny] == 6:
                break

            if maps[nx][ny] == 0:
                maps[nx][ny] = 1



def choose(idx, cnt):
    global min_val, cctv_cnt

    if cnt == cctv_cnt:
        min_val = min(min_val, watching())
        return
    
    temp = copy.deepcopy(cnt)
    x,y,num = cctv[idx]
    for d in cctv_direction[num]:
        watching(temp, d, x, y)
        choose(idx+1, temp)
        temp = copy.deepcopy(cnt)

choose(0, maps)
print(min_val)
