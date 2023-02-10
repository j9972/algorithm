import heapq
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dik(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dik(start)
cnt = 0
maxDistance = 0
for d in distance:
    if d != INF:
        cnt += 1
        maxDistance = max(d, maxDistance)
print(cnt - 1, maxDistance)

