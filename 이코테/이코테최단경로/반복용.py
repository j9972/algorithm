# 플로이드 - 플로이드 사용
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
data = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            data[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            data[i][j] = min(data[i][j], data[i][k]+data[k][j])

res = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if data[i][j] != INF or data[j][i] != INF:
            count += 1
    if count == n:
        res += 1
print(res)
