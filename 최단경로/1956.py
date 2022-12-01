import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
#distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

maxD = INF
for i in range(1, n+1):
    maxD = min(maxD, graph[i][i])

if maxD == INF:
    print(-1)
else:
    print(maxD)
