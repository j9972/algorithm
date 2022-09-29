# 케빈 베이컨 6단계 법칙
# 플로이드
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

kevin = [0] * (n+1)
ans = INF
for a in range(1, n+1):
    for b in range(1, n+1):
        kevin[a] += graph[a][b]
    if ans > kevin[a]:
        ans = kevin[a]
        res = a
print(res)
