import sys
input = sys.stdin.readline
import heapq

n,m = map(int,input().split())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

start = 1

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dik(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue   
    
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

maxNode = 0
maxDist = 0
dik(start)
res = []

for i in range(1,n+1):
    if distance[i] > maxDist:
        maxNode = i
        maxDist = distance[i]
        res = [maxNode]
    elif distance[i] == maxDist:
        res.append(i)
print(maxNode, maxDist, len(res))

