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

left = 0

virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append((i,j))
        elif arr[i][j] == 0:
            left += 1

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]
ans = []

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and arr[x][y] != 1 and not visited[x][y]

def init_visited():
    for x in range(n):
        for y in range(n):
            visited[x][y] = False

def calc(left):

    q = deque(ans)
    init_visited()
    time = 0

    for x,y in ans:
        visited[x][y] = True

    while q:

        if not left:
            break

        time += 1

        for _ in range(len(q)):
            x,y = q.popleft()

            for dx,dy in zip(dxs, dys):
                nx,ny = x + dx, y + dy

                if can_go(nx,ny):
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    if arr[nx][ny] == 0:
                        left -= 1
    
    if not left:
        return time
    else:
        return sys.maxsize
    
                

def choose(idx, cnt):
    global min_val

    if cnt == m:
        min_val = min(min_val, calc(left))
        return
    if idx >= len(virus):
        return
    
    ans.append(virus[idx])# ans에는 활성화된 바이러스가 들어감
    choose(idx+1, cnt+1)
    ans.pop()
    choose(idx+1, cnt)



choose(0,0)

if min_val == sys.maxsize:
    min_val = -1

print(min_val)