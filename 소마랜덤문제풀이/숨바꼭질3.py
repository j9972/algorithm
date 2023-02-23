#골드5 - 13549
import sys
input = sys.stdin.readline
from collections import deque

start, goal = map(int,input().split())
dist = [0] * 100001

q = deque()
q.append(start)

while q:
    now = q.popleft()

    if now == goal:
        print(dist[goal])
        break

    for i in (now-1,now+1,now*2):
        if 0<=i<100001 and dist[i] == 0:
            if i == now*2:
                dist[i] = dist[now]
            else:
                dist[i] = dist[now] + 1
            q.append(i)
                
