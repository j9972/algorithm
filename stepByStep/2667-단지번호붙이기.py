n = int(input())

arr = [
    list(map(int,input()))
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

size = 0
home_size = []

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y):
    global size

    if in_range(x,y) and arr[x][y]:
        arr[x][y] = 0
        size += 1

        for dx,dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy

            dfs(nx,ny)
        
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j):
            home_size.append(size)
            size = 0
print(len(home_size))
for i in sorted(home_size):
    print(i)