# 실버 1 - 1697
import sys
input = sys.stdin.readline
from collections import deque

start,k = map(int,input().split())
length = 100000

dist = [0] * (length+1)

def bfs():
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        if now == k:
            print(dist[k])
            break
        for i in (now-1,now+1,now*2):
            if 0 <= i <= length and not dist[i]:
                dist[i] = dist[now] + 1
                q.append(i)
bfs()



