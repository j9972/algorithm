# 2644, 실버2
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
start,end = map(int,input().split())

m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

res = [0] * (n+1)
visited = [False] * (n+1)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            res[i] = res[start] + 1
            dfs(i)

# def bfs(start):
#     q = deque([start])
#     visited[start] = True

#     while q:
#         now = q.popleft()

#         for i in graph[now]:
#             if not visited[i]:
#                 q.append(i)
#                 res[i] = res[now] + 1
#                 visited[i] = True

# bfs(start)
dfs(start)
if res[end] > 0:
    print(res[end])
else:
    print(-1)