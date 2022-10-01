# 숨바꼭질
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = 1
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

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

maxNode = 0
maxDistance = 0
res = []

for i in range(1, n+1):
    if distance[i] > maxDistance:
        maxDistance = distance[i]
        maxNode = i
        res = [maxNode]
    elif maxDistance == distance[i]:
        res.append(i)

print(maxNode, maxDistance, len(res))
