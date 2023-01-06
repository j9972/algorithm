from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, distInfo, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[start] = 0

q = deque([start])

while q:
    now = q.popleft()

    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

flag = False
for i in range(1, n+1):
    if distance[i] == distInfo:
        print(i)
        flag = False
if flag:
    print(-1)
