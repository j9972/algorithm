# 상하좌우
import sys
input = sys.stdin.readline

n = int(input())
direction = list(map(str, input().split()))

step = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1

for d in direction:
    for i in range(len(step)):
        if d == step[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if 1 > nx or nx > n or 1 > ny or ny > n:
        continue
    x, y = nx, ny


print(x, y)
