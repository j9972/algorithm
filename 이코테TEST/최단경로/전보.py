import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
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
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dik(start)
cnt = 0
mv = 0
for d in distance:
    if d != INF:
        cnt += 1
        mv = max(mv, d)
print(cnt - 1, mv)
