from collections import deque
import copy
import heapq
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())
INF = int(1e9)
graph = [[]*m for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
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
            if distance[i[0]] < cost:
                cost = distance[i[0]]
                heapq.heappush(q, (cost, i[0]))


dik(start)
cnt = 1
max_distance = 0
for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)
print(cnt - 1, max_distance)
