# 전보 - 개선된 다익스트라
import sys
import heapq
input = sys.stdin.readline

n, m, start = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


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
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

maxDistance = 0
count = 0

for d in distance:
    if d != INF:
        count += 1
        maxDistance = max(maxDistance, d)
print(count - 1, maxDistance)
