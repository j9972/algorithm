# 전보 - 개선된 우선순위 큐
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            # 바로 가는거
            cost = dist + i[1]
            if distance[i[0]] > cost:
                # 현재 지점 찍고 가는거 더 가까운 경우
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
