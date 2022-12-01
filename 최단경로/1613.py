import sys
input = sys.stdin.readline

n, k = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    graph[k][k] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

s = int(input())
for i in range(s):
    a, b = map(int, input().split())

    if graph[a][b] != INF:
        print(-1)
    elif graph[b][a] != INF:
        print(1)
    else:
        print(0)
