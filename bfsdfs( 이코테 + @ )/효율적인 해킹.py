# 1325 , 살버 1
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # m은 간선 같은 역할

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[b].append(a) # a가 b를 신뢰, b 해킹시 a 자동 해킹

def bfs(start):
    cnt = 1 # 지금 해킹한 node를 포함해야 하므로
    visited = [False] * (n+1)
    visited[start] = True
    q = deque([start])

    while q:
        current = q.popleft()

        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                q.append(i)
    return cnt

res = []
max_cnt = 1

for i in range(1,n+1):
    data = bfs(i)
    if data > max_cnt:
        max_cnt = data
        res = [i]
    if data == max_cnt:
        res.append(i)
print(*res)