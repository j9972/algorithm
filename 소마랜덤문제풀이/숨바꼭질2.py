# 골드 4 - 12851
import sys
input = sys.stdin.readline
from collections import deque

start, goal = map(int,input().split())
length = 100001
dist = [0] * length 
cnt = 0

def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    dist[start] = 0

    while q:
        now = q.popleft()

        if now == goal:
            cnt += 1
            continue

        for i in (now-1,now+1,now*2):
            if 0<=i<length and (not dist[i] or dist[i] == dist[now] + 1):
                dist[i] = dist[now] + 1
                q.append(i)

bfs(start)
print(dist[goal])
print(cnt)