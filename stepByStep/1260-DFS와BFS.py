from collections import deque

n,m,v = map(int,input().split())

graph = [
    [] * (n+1)
    for _ in range(n+1)
]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def dfs(start):
    visited1[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited1[i]:
            dfs(i)

def bfs(start):
    visited2[start] = True
    q = deque([start])

    while q:
        data = q.popleft()
        print(data, end=' ')

        for i in graph[data]:
            if not visited2[i]:
                q.append(i)
                visited2[i] = True
                


dfs(v)
print()
bfs(v)
