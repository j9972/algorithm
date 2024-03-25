import sys
from collections import deque

n,m = map(int,input().split())
min_val = sys.maxsize

# 0 : 빈칸, 1 : 벽, 2 : 바이러스
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 빈칸 -> 퍼지는 시간, 벽 -> - , 비활성 : *, 활성 : 0 -> 내 생각은 바이러스 활성 비활성 구분할 필요 없음
temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append((i,j))
#print(virus)

dxs,dys = [-1,1,0,0], [0,0,-1,1]
ans = []

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and temp[x][y] != '-'

def init_temp():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                temp[i][j] = '-'
            elif arr[i][j] == 2:
                temp[i][j] = '*'
            else:
                temp[i][j] = -1

def find_max_val():
    max_val = 0

    for i in range(n):
        for j in range(n):
            if temp[i][j] != '-' and temp[i][j] != '*':
                if temp[i][j] == 0:
                    return -1
                max_val = max(max_val, temp[i][j])

    return max_val

def calc():
    
    for i in ans:
        x,y = i
        
        for dx,dy in zip(dxs,dys):
            nx,ny = x + dx, y + dy

            if can_go(nx,ny):
                if temp[nx][ny] == -1:
                    if temp[x][y].isdigit():
                        temp[nx][ny] = temp[x][y] + 1
                    elif temp[x][y] == '*':
                        temp[nx][ny] = 1

    return find_max_val()
                

def choose(idx, cnt):
    global min_val


    if cnt == m:
        min_val = min(min_val, calc())
        return
    if idx >= len(virus):
        return
    
    ans.append(virus[idx])# ans에는 활성화된 바이러스가 들어감
    choose(idx+1, cnt+1)
    ans.pop()
    choose(idx+1, cnt)

init_temp()

choose(0,0)

if min_val == sys.maxsize:
    min_val = -1

print(min_val)