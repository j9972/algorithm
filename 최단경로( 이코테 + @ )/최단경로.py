import sys
import heapq
input = sys.stdin.readline

n,e = map(int,input().split())
start = int(input())

INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(e):
    a,cost,b = map(int,input().split())
    graph[a].append((cost,b))

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

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])