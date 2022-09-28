import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [[INF]*k for _ in range(n+1)]

for _ in range(m):
    a, b, c, = map(int, input().split())
    graph[a].append([b, c])

start = 1
q = []


def dij(start):
    distance[start][0] = 0
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)
        for i, j in graph[now]:  # i[0] == j
            cost = dist + j
            if distance[i][k-1] > cost:
                distance[i][k-1] = cost
                distance[i].sort()
                heapq.heappush(q, [cost, i])


dij(start)

for i in range(1, n+1):
    if distance[i][k-1] == INF:
        print(-1)
    else:
        print(distance[i][k-1])
