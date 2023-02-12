# silver 1 - 5014
from collections import deque
import sys
input = sys.stdin.readline

n, start, end, up, down = map(int, input().split())

d = [-1] * (n+1)
d[start] = 0
q = deque()
q.append(start)

while q:
    now = q.popleft()

    if now == end:
        print(d[now])
        exit(0)

    for nx in [now - down, now + up]:
        if 0 < nx <= n and d[nx] == -1:
            q.append(nx)
            d[nx] = d[now] + 1

print('use the stairs')
