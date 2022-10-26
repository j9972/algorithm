from collections import deque

n, m, k, x = map(int, input().split())

data = [[] * (m+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)

queue = deque([x])

distance = [-1] * (n+1)
distance[x] = 0

while queue:
    now = queue.popleft()

    for next in data[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

find = False

for i in range(1, n+1):
    if distance[i] == k:
        find = True
        print(i)

if find == False:
    print(-1)
