n = int(input())
m = int(input())

graph = [
    [] * (n+1)
    for _ in range(n+1)
]

for _ in  range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

start = 1

visited = [False] * (n+1)

def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

dfs(start)

cnt = 0
for i in visited:
    if i:
        cnt += 1

print(cnt - 1)