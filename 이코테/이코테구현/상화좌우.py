import sys
input = sys.stdin.readline

n = int(input())
x, y = 1, 1
array = input().split()

direction = ['L', 'U', 'R', 'D']

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for plan in array:
    for i in range(len(direction)):
        if plan == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
