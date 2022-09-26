# 숨바꼭질.  술래는 항상 1번에서 출발 -> 개선된 다익스트라

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
start = 1

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

maxNode = 0
maxDistance = 0

res = []

for i in range(1, n+1):
    if maxDistance < distance[i]:
        maxNode = i
        maxDistance = distance[i]
        res = [maxNode]
    elif maxDistance == distance[i]:
        res.append(i)

print(maxNode, maxDistance, len(res))
