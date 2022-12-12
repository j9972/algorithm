# 상하좌우
import sys
input = sys.stdin.readline

n = int(input())
data = [[0] * (n+1) for _ in range(n+1)]

direction = list(map(str, input().split()))

x, y = 1, 1
for i in range(len(direction)):
    data[x][y] = 1
