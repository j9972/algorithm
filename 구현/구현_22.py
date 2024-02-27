dxs, dys = [-1,0,0,1], [0,-1,1,0]

mapper = {
    "U" : 0,
    "L" : 1,
    "R" : 2,
    "D" : 3
}

grid = [
    [-1 for _ in range(4001)]
    for _ in range(4001)
]

def in_range(x,y):
    return 0<=x<4001 and 0<=y<4001

for tc in range(int(input())):

    n = int(input())
    arr = list()

    for num in range(1, n+1):
        x, y, w, d = input().split()
        i, j, w = (-int(y)) * 2 + 2000, int(x) * 2 + 2000, int(w)

        arr.append((num, i, j, w, mapper[d]))

    record = -1

    for t in range(1,4001):
        next_arr = []

        for i in arr:
            num, x, y, w, d = i         
            nx,ny = x + dxs[d], y + dys[d]

            if in_range(nx,ny):
                if grid[nx][ny] == -1:

                    next_arr.append((num, nx,ny, w, d))
                    grid[nx][ny] = len(next_arr) - 1
                
                else:
                    record = t
                    # 무게가 크면
                    if next_arr[grid[nx][ny]][3] < w:
                        next_arr[grid[nx][ny]] = (num, nx, ny, w, d)
                    # 무게가 같고 번호가 크면
                    elif next_arr[grid[nx][ny]][3] == w and next_arr[grid[nx][ny]][0] < num:
                        next_arr[grid[nx][ny]] = (num, nx, ny, w, d)

        arr = next_arr[:]

        for i in next_arr:
            grid[i[1]][i[2]] = -1
    print(record)