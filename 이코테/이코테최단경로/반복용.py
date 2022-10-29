# 전보
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

res = 0
for a in range(1, n+1):
    count = 0
    for b in range(1, n+1):
        if graph[a][b] != INF or graph[b][a] != INF:
            count += 1
    if count == n:
        res += 1

print(res)
