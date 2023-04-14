import sys
import heapq
input = sys.stdin.readline

n,d = map(int,input().split())

INF = int(1e9)

graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

for i in range(d):
    graph[i].append((i+1,1))

for i in range(n):
    s,e,dist = map(int,input().split())
    if e <= d:
        graph[s].append((e,dist))

start = 0

def dik(start):
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

dik(start)

print(distance[d])