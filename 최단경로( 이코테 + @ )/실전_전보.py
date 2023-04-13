import sys
input = sys.stdin.readline
import heapq

n,e,start = map(int,input().split())

INF= int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(e):
    start,end,cost = map(int,input().split())
    graph[start].append((end,cost))

q = []
heapq.heappush(q,(0,start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))


cnt = 0
max_dist = 0
for i in distance:
    if i != INF:
        cnt += 1
        max_dist = max(max_dist, i)
print(cnt-1, max_dist)
