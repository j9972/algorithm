import sys
input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b]==1):
                graph[a][b] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()
        
        