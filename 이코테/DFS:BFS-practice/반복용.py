from collections import deque
import sys
sys.setrecursionlimit(10**9)

n, m, k, x = map(int, input().split())

data = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)

queue = deque([x])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distance = [-1] * (n+1)
distance[x] = 0

while queue:
    now = queue.popleft()

    for next in data[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

check = False
# 1부터 n번까지의 도시를 이동하기에 range 범위가 이렇게 된다.
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
