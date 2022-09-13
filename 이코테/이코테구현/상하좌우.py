n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

moves = ['L', 'R', 'U', 'D']

for plan in plans:
    if 1 <= nx <= n and if 1 <= ny <= n:
        for i in range(len(moves)):
            if plan == moves[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        x, y = nx, ny
print(x, y)
