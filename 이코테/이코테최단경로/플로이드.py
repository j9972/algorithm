import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 최소 거리 단선만 구하면 되기때문에 크기 비교를 해야한다
for i in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')

    print()
