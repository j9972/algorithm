import sys
input = sys.stdin.readline
from collections import deque

n,m,k,start = map(int,input().split())

graph = [[] for _ in range(n+1)]

INF = int(1e9)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

distance = [INF] * (n+1)
distance[start] = 0

q = deque([start])

while q:
    now = q.popleft()

    for next in graph[now]:
        if distance[next] == INF:
            distance[next] = distance[now] + 1
            q.append(next)

check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)
