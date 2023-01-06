from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

data = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()

    for next in data[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

flag = False
for i in range(1, n+1):  # 노드가 1 ~ n 까지니까 이 범위가 나오는게 맞다
    if distance[i] == k:
        print(i)
        flag = True

if flag == False:
    print(-1)
