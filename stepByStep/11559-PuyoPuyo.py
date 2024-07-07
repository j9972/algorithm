from collections import deque

arr = [
    list(input())
    for _ in range(12)
]

ans = 0

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<12 and 0<=y<6

def bfs(x,y):
    q = deque()
    q.append((x,y))

    pos = []

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy

            if in_range(nx,ny) and not visited[nx][ny]:
                if arr[x][y] == arr[nx][ny]:
                    q.append((nx,ny))
                    pos.append((nx,ny))
                    visited[nx][ny] = True

    if len(pos) >= 4:
        for i, j in sorted(pos, key=lambda x :(x[1], x[0])):
            boom.append([i,j])
            arr[i][j] = '.'


while True:

    boom = []
    visited = [
        [False] * 6
        for _ in range(12)
    ]

    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and not visited[i][j]:
                bfs(i,j)
    
    if len(boom) == 0:
        break

    for b in boom:
        x,y = b[0], b[1]
        for i in range(x,0,-1):
            arr[i][y] = arr[i-1][y]
        arr[0][y] = '.'
    
    ans += 1

print(ans)