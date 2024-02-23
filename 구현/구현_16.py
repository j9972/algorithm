# 연속적인 폭발
n,m,x,y = map(int,input().split())

x -= 1
y -= 1

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

arr[x][y] = 1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dxs, dys = [-1,1,0,0], [0,0,-1,1]

for t in range(m):
    dist = 2 ** t
    
    new_arr = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                for dx,dy in zip(dxs, dys):
                    nx ,ny = i + dx * dist, j + dy * dist

                    if not in_range(nx,ny):
                        continue

                    new_arr[nx][ny] = 1

    for i in range(n):
        for j in range(n):
            if new_arr[i][j]:
                arr[i][j] = 1
    
val = 0
for i in range(n):
    for j in range(n):
        val += arr[i][j]
print(val)