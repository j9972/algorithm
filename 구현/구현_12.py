n, x,y = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

x -= 1
y -= 1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dxs, dys = [-1,1,0,0], [0,0,-1,1]

ans = [arr[x][y]]
max_val = arr[x][y]
max_pos = (x,y)

while True:

    flag = True

    for dx, dy in zip(dxs, dys):
        nx,ny = x + dx, y + dy

        if not in_range(nx,ny):
            continue
        
        if arr[nx][ny] > max_val:
            flag = False
            max_val = arr[nx][ny]
            max_pos = (nx,ny)
            ans.append(max_val)
            break
    
    if flag:
        break
    x,y = max_pos

for i in ans:
    print(i,end = ' ')
