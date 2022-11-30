# 플로이드
import heapq
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

INF = int(1e9)
n = int(input())
m = int(input())

data = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    if c < data[a][b]:
        data[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            data[i][j] = 0


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            data[i][j] = min(data[i][j], data[i][k]+data[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if data[i][j] == INF:
            print(0, end=' ')
        else:
            print(data[i][j], end=' ')
    print()
