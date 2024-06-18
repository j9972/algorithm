from collections import deque

n, k = map(int, input().split()) 
q = deque()
q.append(n) 
d = [-1 for _ in range(100001)]
d[n] = 0

while q:
    now = q.popleft()
    if now == k:
        print(d[now])
        break
    
    if 0 <= now-1 < 100001 and d[now-1] == -1:
        d[now-1] = d[now] + 1
        q.append(now-1)

    if 0 < now*2 < 100001 and d[now*2] == -1:
        d[now*2] = d[now]
        q.appendleft(now*2)  
        
    if 0 <= now+1 < 100001 and d[now+1] == -1:
        d[now+1] = d[now] + 1
        q.append(now+1)