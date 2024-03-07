import sys
from collections import deque

n,m = map(int,input().split())
x,y,d = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

# 북 동 남 서 (상 우 하 좌)
dxs,dys = [-1,0,1,0],[0,1,0,-1]
q = deque()

visited[x][y] = True
q.append((x,y,d))

ans = 0

def can_go(nx,ny): # 회전시키기
    return in_range(nx,ny) and arr[nx][ny] == 0 and not visited[nx][ny]

def cntClean():
    global ans
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                ans += 1

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs():

    while q:
        x,y,d = q.popleft()

        for _ in range(4):
            d = (d+3) %4
            nx,ny = x + dxs[d], y + dys[d]

            if not can_go(nx,ny):
                continue

            visited[nx][ny] = True
            q.append((nx,ny,d))
            break

        else:
            temp_d = (d+2) % 4
            nx,ny = x + dxs[temp_d], y + dys[temp_d]
            
            if not in_range(nx,ny) or arr[nx][ny]:
                return
            
            q.append((nx,ny,d))

        

bfs()
cntClean()
print(ans)


# def bfs(x, y, d):
#     queue = deque([(x, y, d)])
#     visited[x][y] = True
#     cnt = 1

#     while queue:
#         x, y, d = queue.popleft()
#         temp_d = d

#         for _ in range(4):  # 4방향 검사
#             temp_d = (temp_d + 3) % 4  # 현재 방향에서 왼쪽 방향으로 회전
#             nx, ny = x + dx[temp_d], y + dy[temp_d]

#             if not(0 <= nx < n and 0 <= ny < m):  # 범위를 벗어나면 다음 방향으로
#                 continue

#             if arr[nx][ny] == 0 and not visited[nx][ny]:  # 청소할 수 있는 공간이면
#                 visited[nx][ny] = True
#                 cnt += 1
#                 queue.append((nx, ny, temp_d))
#                 break

#         else:  # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
#             back_d = (d + 2) % 4
#             nx, ny = x + dx[back_d], y + dy[back_d]

#             if not(0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == 1:  # 뒤쪽이 벽이거나 범위를 벗어난 경우
#                 return cnt

#             queue.append((nx, ny, d))  # 후진
#     return cnt

# result = bfs(x, y, d)
# print(result)
