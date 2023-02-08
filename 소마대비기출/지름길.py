# 실버 1 - 1446
import heapq
import sys
input = sys.stdin.readline

n, d = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(d+1)]

for i in range(d):
    graph[i].append((i+1, 1))  # 1씩 증가하는 것을 보여줌

for i in range(n):
    s, e, length = map(int, input().split())
    if e <= d:
        graph[s].append((e, length))

distance = [INF] * (d+1)

q = []
heapq.heappush(q, (0, 0))
distance[0] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue
    for x in graph[now]:
        cost = x[1] + dist
        if cost < distance[x[0]]:
            distance[x[0]] = cost
            heapq.heappush(q, (cost, x[0]))

print(distance[d])
