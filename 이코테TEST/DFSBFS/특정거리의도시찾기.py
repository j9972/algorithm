from collections import deque
import sys
input = sys.stdin.readline

n, m, k, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([start])
distance = [-1] * (n+1)
distance[start] = 0

while q:
    now = q.popleft()

    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

res = []
for i in range(n+1):
    if distance[i] == k:
        res.append(i)
res.sort()
if len(res) == 0:
    print(-1)
else:
    for i in res:
        print(i, end=' ')
    print()
