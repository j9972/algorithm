OFFSET = 1000

arr = [
    list(map(int,input().split()))
    for _ in range(2)
]

temp = [
    [0 for _ in range(2001)]
    for _ in range(2001)
]

for i, (x1,y1,x2,y2) in enumerate(arr, start = 1):
    x1,y1 = x1 + OFFSET, y1 + OFFSET
    x2,y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
            temp[x][y] = i

min_x, min_y, max_x, max_y = 2001,2001,0,0

for i in range(2001):
    for j in range(2001):
        if temp[i][j] == 1:
            min_x = min(min_x,i)
            min_y = min(min_y,j)
            max_x = max(max_x,i)
            max_y = max(max_y,j)

if (min_x,min_y,max_x,max_y) != (2001,2001,0,0):
    print((max_x-min_x+1) * (max_y-min_y+1))
else:
    print(0)
    