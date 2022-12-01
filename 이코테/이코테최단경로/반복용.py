# 플로이드 - 플로이드 사용
import heapq
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

start = 1

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dik(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

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

maxNode = 0
maxDist = 0
res = []

for i in range(1, n+1):
    if maxDist < distance[i]:
        maxDist = distance[i]
        maxNode = i
        res = [maxNode]
    elif maxDist == distance[i]:
        res.append(i)

print(maxNode, maxDist, len(res))
