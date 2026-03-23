import sys
input = sys.stdin.readline

n = int(input())
connect = int(input())

graph = [
    []
    for _ in range(n+1)
]

for _ in range(connect):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

visited[1] = True

def dfs(val):
    visited[val] = True
    for i in graph[val]:
       if not visited[i]:
           dfs(i)

dfs(1)

cnt = 0
for i in range(1,n+1):
    if visited[i]:
        cnt += 1
print(cnt - 1)