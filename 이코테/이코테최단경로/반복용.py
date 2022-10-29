# 전보
import heapq
from itertools import count
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())  # 도시개수, 간선개수, 메시지를 보내고자 하는 도시
INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dij(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dij(start)

count = 0
maxD = 0

for d in distance:
    if d != INF:
        count += 1
        maxD = max(maxD, d)

print(count-1, maxD)
