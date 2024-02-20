from collections import deque

n,k = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

r,c = map(int,input().split())

r -= 1
c -= 1

ans_x, ans_y = r,c

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y,val):
    if not in_range(x,y):
        return False
    if visited[x][y] or arr[x][y] >= val:
        return False
    return True

dxs, dys = [-1,1,0,0], [0,0,-1,1]

def bfs(value):
    global max_val, max_pos

    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx,ny, value):
                visited[nx][ny] = True
                q.append((nx,ny))
                max_val = max(max_val, arr[nx][ny])
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] and arr[i][j] == max_val:
                max_pos.append((i,j))
            


for _ in range(k):

    q = deque()

    max_val, max_pos = 0, []

    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    visited[r][c] = True
    q.append((r,c))
    bfs(arr[r][c])

    if not max_pos:
        break

    max_pos.sort(key = lambda x : (x[0], x[1]))

    r,c = max_pos[0]
    ans_x, ans_y = max_pos[0] 
        
print(ans_x + 1, ans_y + 1)