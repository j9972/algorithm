import sys

n = int(input())

max_val = -sys.maxsize

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

boom_cnt = 0
boom = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            boom.append((i,j))
            boom_cnt += 1

temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

ans = list()

boom_type_1 = [(-2,0),(-1,0),(1,0),(2,0)]
boom_type_2 = [(0,-1),(-1,0),(1,0),(0,1)]
boom_type_3 = [(-1,-1),(-1,1),(1,-1),(1,1)]

def init_temp():
    global temp

    for i in range(n):
        for j in range(n):
            temp[i][j] = 0

def getSize():
    val = 0
    for i in range(n):
        for j in range(n):
            if temp[i][j]:
                val += 1
    return val

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def calc():
    init_temp()

    for i in ans:
        x,y,k = i

        temp[x][y] = 1

        if k == 1:
            for dx,dy in boom_type_1:
                nx,ny = x + dx, y + dy

                if not in_range(nx,ny) or temp[nx][ny]:
                    continue

                temp[nx][ny] = 1
        elif k == 2:
            for dx,dy in boom_type_2:
                nx,ny = x + dx, y + dy

                if not in_range(nx,ny) or temp[nx][ny]:
                    continue

                temp[nx][ny] = 1
        elif k == 3:
            for dx,dy in boom_type_3:
                nx,ny = x + dx, y + dy

                if not in_range(nx,ny) or temp[nx][ny]:
                    continue

                temp[nx][ny] = 1

    cnt =  getSize()
    return cnt
                

def choose(cnt):
    global max_val

    if cnt == boom_cnt:
        max_val = max(max_val, calc())
        return

    for k in range(1,4):
        x,y = boom[cnt]

        ans.append((x,y,k))
        choose(cnt+1)
        ans.pop()

choose(0)
print(max_val)