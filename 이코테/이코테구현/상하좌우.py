n = int(input())
plans = input().split()
direction = ['L', 'R', 'U', 'D']

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(direction)):
        if plan == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if 1 > nx or 1 > ny or n < nx or n < ny:
        continue

    x, y = nx, ny

print(x, y)
