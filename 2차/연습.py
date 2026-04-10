import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

n,m = map(int,input().split())

arr = [i for i in range(101)]
visited = [False for i in range(101)]

for _ in range(n+m):
    s,e = map(int,input().split())

    arr[s] = e

q = deque()
q.append((1,0))
visited[1] = True

while q:
    now, cnt = q.popleft()

    if now == 100:
        print(cnt)
        break

    for i in range(1,7):
        nx = now + i

        if nx > 100:
            continue

        nx = arr[nx]

        if not visited[nx]:
            visited[nx] = True
            q.append((nx, cnt + 1))


