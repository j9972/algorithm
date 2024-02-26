n,m, t, k = map(int,input().split())

mapper = {
    "U" : 0,
    "R" : 1,
    "L" : 2,
    "D" : 3
}

arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for i in range(m):
    x, y, d, v = input().split()
    x,y,v = int(x),int(y),int(v)

    arr[x - 1][y - 1].append((v, i + 1, mapper[d]))

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def move(x,y,v,d):
    dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]

    for _ in range(v):
        nx,ny = x + dx[d], y + dy[d]

        if not in_range(nx,ny):
            d = 3 - d
            nx,ny = x + dx[d], y + dy[d]
        x,y = nx,ny
    
    return (nx,ny,d)

def move_all():
    for x in range(n):
        for y in range(n):
            for v, num, move_dir in arr[x][y]:
                next_x, next_y, next_dir = move(x, y, v, move_dir)
                temp[next_x][next_y].append((v, num, next_dir))

def change():
    for i in range(n):
        for j in range(n):
            if len(temp[i][j]) >= k:
                temp[i][j].sort(lambda x: (-x[0], -x[1]))
                while len(temp[i][j]) > k:
                    temp[i][j].pop()

for _ in range(t):
    temp = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    move_all()
    change()

    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]

val = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            val += len(arr[i][j])
print(val)