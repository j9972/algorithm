# 전보
import heapq
import sys
from turtle import distance
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


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

count = 0
maxDistance = 0


for d in distance:
    if d != INF:
        count += 1
        maxDistance = max(d, maxDistance)
print(count - 1, maxDistance)
