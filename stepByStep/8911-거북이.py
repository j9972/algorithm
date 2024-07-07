tc = int(input())

# 북 동 남 서
dxs, dys = [-1,0,1,0], [0,1,0,-1]

for _ in range(tc):
    way = input()
    x,y,max_x,min_x,max_y,min_y= 0,0,0,0,0,0
    direct = 0

    for j in way:
        if j == 'F':
            x,y = x + dxs[direct], y + dys[direct]
        elif j == 'B':
            x,y = x - dxs[direct], y - dys[direct]
        elif j == 'L':
            direct -= 1
            direct %= 4
        elif j == 'R':
            direct += 1
            direct %= 4
    
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        min_x = min(x, min_x)
        min_y = min(y, min_y)
    print((max_x - min_x) * (max_y - min_y))
