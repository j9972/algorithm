import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = 0

graph = [
    [] for _ in range(n+1)
]

visited = [False] * (n+1)

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)