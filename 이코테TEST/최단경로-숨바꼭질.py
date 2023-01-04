import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dik(start):
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


dik(1)

node, maxDistance = 0, 0
res = []

for i in range(1, n+1):
    if distance[i] > maxDistance:
        node = i
        maxDistance = distance[i]
        res = [i]
    elif distance[i] == maxDistance:
        res.append(i)
print(node, maxDistance, len(res))
