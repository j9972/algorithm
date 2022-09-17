from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k, x = list(map(int, input().split()))

board = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

queue = deque([x])

while queue:
    now = queue.popleft()

    for next in board[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        check = True
        print(i)
if check == False:
    print(-1)
