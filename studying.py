# 1507
import sys
input = sys.stdin.readline

n = int(input())

INF = int(1e9)

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

road = [[True] * n for _ in range(n)]

res = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            if k == a or a == b or b == k:
                continue
            if graph[a][b] == graph[a][k]+graph[k][b]:
                road[a][b] = False
            elif graph[a][b] > graph[a][k]+graph[k][b]:
                res = -1

# 최솟값이라면
if res != -1:
    for i in range(n):
        for j in range(i, n):
            if road[i][j]:
                res += graph[i][j]
print(res)
