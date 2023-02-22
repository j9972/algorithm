# 실버 1 - 경로 찾기

import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 1 or (graph[a][k] == 1 and  graph[k][b] == 1):
                graph[a][b] = 1
            
for i in graph:
    for j in i:
        print(j, end=' ')
    print()
