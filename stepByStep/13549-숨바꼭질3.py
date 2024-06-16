import sys
from collections import deque

n,k = map(int,input().split())

d = [-1] * 100001

q = deque()
q.append(n)
d[n] = 0

while q:
    now = q.popleft()

    if now == k:
        break

    for i in [now+1, now-1, now*2]:
        if 0 <= i < 100001 and d[i] == -1:
            if i == now * 2:
                d[i] = d[now]
                q.appendleft(i)
            else:
                d[i] = d[now] + 1
                q.append(i)

print(d[k])