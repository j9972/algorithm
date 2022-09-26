# 전보는 우선순위 큐 ( 개선된 다익스트라 문제 ) 이다

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

# 1차원 리스트 초기화
graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a-> b까지 비용이 c
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
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

count = 0
maxDistance = 0

for d in distance:
    if d != INF:
        count += 1
        maxDistance = max(maxDistance, d)

print(count - 1, maxDistance)
