import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0


for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

for r in graph:
    for c in r:
        print(c, end=' ')
    print()
