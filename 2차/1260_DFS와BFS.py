import sys
input = sys.stdin.readline

from collections import deque

n,m,v = map(int,input().split())

graph = [
    [] * (n+1)
    for _ in range(n+1)
]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

visited = [False] * (n+1)

def dfs(start):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

visited2 = [False] * (n+1)

def bfs(start):
    q = deque([start])
    visited2[start] = True

    while q:
        v = q.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not visited2[i]:
                visited2[i] = True
                q.append(i)
dfs(v)
print()
bfs(v)
