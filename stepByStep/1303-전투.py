n,m = map(int,input().split())

arr = [
    list(input())
    for _ in range(n)
]

a_total, b_total = 0, 0
size = 0

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<m


def dfs(x,y,target):
    global size

    if in_range(x,y) and arr[x][y] == target:
        arr[x][y] = 'S'
        size += 1

        for dx,dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy

            dfs(nx,ny,target)

        return True
    
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j,'W'):
            a_total += size ** 2
            size = 0
        if dfs(i,j,'B'):
            b_total += size ** 2
            size = 0

print(a_total, b_total)