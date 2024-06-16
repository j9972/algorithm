from collections import deque

n,k = map(int,input().split())

d = [0] * 100001

q = deque()
q.append(n)

times, cnt = 0,0

while q:
    now = q.popleft()

    if now == k:
        times = d[now]
        cnt += 1
        continue

    for i in [now+1, now-1, now*2]:
        if 0 <= i < 100001 and (d[i] == 0 or d[i] == d[now] + 1):
            d[i] = d[now] + 1
            q.append(i)

print(times)
print(cnt)