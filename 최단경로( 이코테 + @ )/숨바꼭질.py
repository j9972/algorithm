import sys
import heapq
input = sys.stdin.readline

n, edge = map(int,input().split())

INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(edge):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

start = 1

def dik(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

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

res = []
node = 0
max_dist = 0

for i in range(1,n+1):
    if max_dist < distance[i]:
        node = i
        max_dist = distance[i]
        res = [i]
    elif max_dist == distance[i]:
        res.append(i)
print(node, max_dist, len(res))