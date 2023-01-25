import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
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
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dik(start)

cnt = 0
max_distance = 0

for d in distance:
    if d != INF:
        max_distance = max(d, max_distance)
        cnt += 1
print(cnt-1, max_distance)
