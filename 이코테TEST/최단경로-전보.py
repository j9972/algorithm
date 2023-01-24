import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # i[0] 는 목적지, i[1] 은 비용


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


dik(start)
cnt = 0
max_distance = 0

for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(d, max_distance)

print(cnt - 1, max_distance)
